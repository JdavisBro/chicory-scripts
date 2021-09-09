import argparse
import base64
import codecs
import json
import os
import zlib

from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("image",help="Image file to turn into Geo.")
parser.add_argument("-l","--level",help="Level to edit the geo of.")
args = parser.parse_args()

im = Image.open(args.image).convert("RGB")

palette = {(6, 33, 0): 0, (252, 255, 66): 1, (84, 56, 0): 2, (255, 148, 244): 3, (181, 181, 181): 4, (255, 0, 0): 5, (0, 95, 133): 6, (0, 252, 185): 7, (0, 230, 168): 8, (0, 191, 140): 9, (0, 150, 110): "A", (0, 87, 64): "B", (45, 242, 0): "C", (39, 212, 0): "D", (29, 156, 0): "E", (16, 87, 0): "F"}

layers = ["7","8","9","A","B","C","D","E","F"]

geodata = list(im.getdata())

paintdata = ""

for pixel in geodata:
    if pixel in palette:
        paintdata += "F" if str(palette[pixel]) in layers else "0"
        paintdata += str(palette[pixel])
    else:
        # why did you do that...
        paintdata += "00"

# NOW to turn it into geo

paintdata = codecs.decode(paintdata,"hex_codec") # to bytes
paintdata = zlib.compress(paintdata) # compress
paintdata = base64.b64encode(paintdata).decode("utf-8") # base 64 encode

print(paintdata)

if os.path.exists("Chicory A Colorful Tale") and args.level:
    with open("Chicory A Colorful Tale/PC/level_data") as f:
        levels = json.load(f)
    levels[args.level]["geo"] = paintdata
    with open("Chicory A Colorful Tale/PC/level_data","w") as f:
        json.dump(levels,f)