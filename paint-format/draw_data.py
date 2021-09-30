import argparse
import base64
import json
import os
import random
import sys
import zlib

from PIL import Image
from PIL.ImageColor import getrgb

# Install pillow and
# Run this from command line:
# py draw_data.py
# or
# python3 draw_data.py

parser = argparse.ArgumentParser()
parser.add_argument("screen",help="The screen to turn into an image.")
parser.add_argument("-p","--paint",help="Save image of your paint.",action="store_true")
parser.add_argument("-g","--geo",help="Save image of geo.",action="store_true")
parser.add_argument("-a","--actual-geo",help="Export actual geo and not smaller",action="store_true")
parser.add_argument("-s","--save",help="Location of your _playdata file.")
parser.add_argument("-l","--level-data",help="Location of your level_data file.")
args = parser.parse_args()

if len(args.screen.split("_")) != 3:
    print("Invalid Screen Argument. Must be in the format LAYER_X_Y, e.g 1_4_2 (layer is the third line of the save file, x is first and y is second)")

GEO = not args.paint and args.geo # Paint is false and geo is true

if not args.save:
    if sys.platform == "win32" or sys.platform ==  "cygwin":
        saveLocation = os.path.expandvars("%LOCALAPPDATA%/paintdog/save/_playdata")
    elif sys.platform == "darwin":
        saveLocation = os.path.expanduser("~/Library/Application Support/paintdog/save/_playdata")
    elif sys.platform == "linux":
        saveLocation = os.path.expanduser("~/.local/share/Steam/steamapps/compatdata/1123450/pfx/drive_c/users/steamuser/Local Settings/Application Data/paintdog/save/_playdata")
else:
    if sys.platform == "win32" or sys.platform == "cygwin":
        saveLocation = os.path.expandvars(args.save)
    else:
        saveLocation = os.path.expanduser(args.save)
if not args.level_data:
    if sys.platform == "win32" or sys.platform ==  "cygwin":
        levelDataLocation = os.path.expandvars("/Program Files (x86)/Steam/steamapps/common/Chicory A Colorful Tale/PC/level_data")
    elif sys.platform == "darwin":
        levelDataLocation = os.path.expanduser("~/Library/Application Support/Steam/steamapps/common/Chicory A Colorful Tale/PC/level_data")
    elif sys.platform == "linux":
        levelDataLocation = os.path.expanduser("~/.local/share/Steam/steamapps/common/Chicory A Colorful Tale/PC/level_data")
else:
    if sys.platform == "win32" or sys.platform == "cygwin":
        levelDataLocation = os.path.expandvars(args.level_data)
    else:
        levelDataLocation = os.path.expanduser(args.level_data)

if GEO:
    if args.actual_geo:
        size = (162,46)
    else:
        size = (81,46)
    palette = {
        0: getrgb("#062100"), 1: getrgb("#fcff42"), 2: getrgb("#543800"),
        3: getrgb("#ff94f4"), 4: getrgb("#b5b5b5"), 5: getrgb("#FF0000"),
        6: getrgb("#005f85"), 7: getrgb("#00fcb9"), 8: getrgb("#00e6a8"),
        9: getrgb("#00bf8c"), 10: getrgb("#00966e"), 11: getrgb("#005740"),
        12: getrgb("#2df200"), 13: getrgb("#27d400"), 14: getrgb("#1d9c00"),
        15: getrgb("#105700")
    }

    with open(levelDataLocation) as f:
        levelData = json.loads(f.read())
        try:
            allpaint = levelData[args.screen]["geo"]
        except KeyError:
            print("Your screen argument is invalid.")
        del levelData
else:
    size = (162,92)

    with open("palettes.json") as f:
        palettes = json.load(f)

    palette = {0: (0,0,0)}
    i = 0

    for p in palettes:
        if args.screen in palettes[p]["screens"]:
            for c in palettes[p]["colors"]:
                i += 1
                palette[i] = tuple(c)

    with open(saveLocation) as f:
        lines = f.readlines()
        saveData = json.loads(lines[3])
        try:
            allpaint = json.loads(lines[18])[args.screen+".paint"]
        except KeyError:
            print("Either, your screen argument is invalid or the screen you are trying to get hasn't been painted.")
        del lines

    if "custom_color_num" in saveData:
        for customNum in range(int(saveData["custom_color_num"])):
            i += 1
            customNum = int(saveData["custompaint_" + str(customNum)])
            col = (customNum & 255,(customNum >> 8) & 255,(customNum >> 16) & 255)
            palette[i] = col

    del saveData

    with open("paletteExtras.json") as f:
        extras = json.load(f)
    if args.screen in extras:
        palette[15] = tuple(extras[screen])

allpaint = zlib.decompress(base64.b64decode(allpaint)).hex()

paintlist = [[]]

for i, v in enumerate(allpaint):
    paintlist[-1].append(v)
    if (i+1) % size[0] == 0:
        paintlist.append([])

if [] in paintlist:
    paintlist.remove([])

# ok so the way i did this isn't that intuative, paintlist[y][x]

with open("out.txt","w+") as f:
    f.write(allpaint)

im = Image.new("RGB",size,color=(0,0,0))
imData = list(im.getdata())
i = 0
x = 0
for colorlist in paintlist:
    for color in colorlist:
        color = int(color,base=16)
        if GEO and not args.actual_geo:
            x += 1
            if x % 2 != 0:
                continue
        if color in palette:
            imData[i] = palette[color]
        else:
            random.seed(color)
            imData[i] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            random.seed()
        i += 1

os.makedirs("out",exist_ok=True)

im.putdata(imData)
if GEO:
    im.save("out/"+args.screen+".geo.png")
else:
    im.save("out/"+args.screen+".paint.png")
