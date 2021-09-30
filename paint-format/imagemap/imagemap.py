import sys
import os
import json
import base64
import zlib
import codecs
import io

from PIL import Image
from PIL.ImageColor import getrgb
from colorthief import ColorThief

if not os.path.exists(sys.argv[1]):
    print(f"File not found, ({sys.argv[1]})")
    sys.exit()

def nearest_colour( subjects, query ):
    return min( subjects, key = lambda subject: sum( (s - q) ** 2 for s, q in zip( subject, query ) ) )

im2 = Image.open(sys.argv[1]).convert("RGBA")
im = Image.new("RGBA", im2.size, "WHITE") # Remove transparency
im.paste(im2, mask=im2)
im = im.convert("RGB")
del im2

# Map is -6 -7 to 6 7
# Full possible resolution is be 160*13 and 90*15 (as each screen's paint resolution is 160x90)
# 2080 x 1350

divisor = 1 # What the full resolution is divided by (to make it faster)

screen_size = (int(160/divisor),int(90/divisor))

im = im.resize((int(screen_size[0]*13),int(screen_size[1]*15)),resample=Image.NEAREST)

palette = []

# Get first 8 colours and set them as custom, then use the closest colours after.

print("Getting colours.")

byt = io.BytesIO()
im.save(byt,format="png")
cf = ColorThief(byt)
palette = cf.get_palette(color_count=8) + [(255,255,255)]
del cf, byt

im = im.convert("RGB")
im_data = list(im.getdata())
totalPixels = len(im_data)

for i,pixel in enumerate(im_data):
    #print("\r",f" | {str(i)}/{str(totalPixels)} - {str(round(i/totalPixels*100,2))}%",end="") # I think printing slows it down a lot.
    im_data[i] = nearest_colour(palette,pixel)
im.putdata(im_data)
del im_data

# We have the image in Chicory colors (yay)
# Now open default save data :) (i don't want to modify user save data especially since this is modifying the paint)

print("\nSetting Custom Colours")

with open("default_save") as f: # Perhaps make this an absolute path to the script file ?? (is a good idea to do this)
    save = f.readlines()

allpaint = {}

with open("../palettes.json") as f:
    gamepalettes = json.load(f)

def rgbToDec(r, g, b): # gamemaker is bgr for some reason....
    return (b << 16) + (g << 8) + r

actualsavething = json.loads(save[3])
for i,color in enumerate(palette):
    print(rgbToDec(*color),color)
    actualsavething["custompaint_"+str(i)] = rgbToDec(*color)
actualsavething["custom_color_num"] = len(palette)
actualsavething["custom_color_max"] = len(palette)
save[3] = json.dumps(actualsavething) + "\n"

print("Setting Save Paint.")

crop_pos = [0,0]
for y in range(-7,8):
    for x in range(-6,7): # For all the screens on the map
        for p in gamepalettes:
            if f"0_{x}_{y}" in gamepalettes[p]["screens"]:
                colorlen = len(gamepalettes[p]["colors"])+1
        paint = ""
        im_crop = im.crop(box=(crop_pos[0],crop_pos[1],crop_pos[0]+screen_size[0],crop_pos[1]+screen_size[1])) # Crop image to area we need
        im_crop = im_crop.resize((162,92),resample=Image.NEAREST)
        for pixel in im_crop.getdata(): # Convert to hex
            if pixel != (255,255,255):
                paint += hex(colorlen+palette.index(pixel))[2]
            else:
                paint += "0"
        paint = codecs.decode(paint,"hex_codec") # to bytes
        paint = zlib.compress(paint) # compress
        paint = base64.b64encode(paint).decode("utf-8") # base 64 encode
        allpaint[f"0_{x}_{y}.paint"] = paint # Set Paint Data

        crop_pos[0] += screen_size[0] # Update crop pos
    crop_pos[0] = 0
    crop_pos[1] += screen_size[1]

save[18] = json.dumps(allpaint) + "\n"

with open("_playdata","w+") as f:
    f.writelines(save)

im.save("out_"+sys.argv[1])