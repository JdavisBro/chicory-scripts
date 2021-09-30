import sys
import os
import json
import base64
import zlib
import codecs
import io
from math import sqrt

from PIL import Image, ImagePalette
from colorthief import ColorThief

divisor = 1 # What the full resolution is divided by (to make it faster)

screen_size = (int(160/divisor),int(90/divisor))

# Map is -6 -7 to 6 7
# Full possible resolution is be 160*13 and 90*15 (as each screen's paint resolution is 160x90)
# 2080 x 1350

def nearest_colour(subjects,query):
    r, g, b = query
    color_diffs = []
    for color in subjects:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

def rgbToDec(r, g, b):
    return (b << 16) + (g << 8) + r # gamemaker is bgr for some reason....

def main():
    print("Hi :)")

    if not os.path.exists(sys.argv[1]):
        print(f"File not found, ({sys.argv[1]})")
        sys.exit()

    print("Getting palette.")


    im2 = Image.open(sys.argv[1]).convert("RGBA") # Open image as RGBA
    im = Image.new("RGBA", im2.size, "WHITE")
    im.paste(im2, mask=im2) # Remove transparency
    im = im.convert("RGB") # Make RGB
    del im2

    im = im.resize((int(screen_size[0]*13),int(screen_size[1]*15)),resample=Image.NEAREST) # Resize to correct size

    # Colorthief to get palette

    byt = io.BytesIO() # The image needs to be bytes to open with colorthief because for some reason it doesn't accept an already opened pil image
    im.save(byt,format="png")
    cf = ColorThief(byt)
    palette = cf.get_palette(color_count=8) + [(255,255,255)] # Luckily colorthief doesn't get white lmao
    del cf, byt
    im = im.convert("RGB")

    # We have the palette (yay)

    print("Converting colours and creating paint data. (This will take some time)")

    allpaint = {}

    with open("../palettes.json") as f: # Open palettes to know where customs start in each room
        gamepalettes = json.load(f)

    crop_pos = [0,0]
    for y in range(-7,8):
        for x in range(-6,7): # For all the screens on the map
            for p in gamepalettes:
                if f"0_{x}_{y}" in gamepalettes[p]["screens"]:
                    colorlen = len(gamepalettes[p]["colors"])+1 # Get amount of colours in rooms palette to know where customs start.
            im_crop = im.crop(box=(crop_pos[0],crop_pos[1],crop_pos[0]+screen_size[0],crop_pos[1]+screen_size[1])) # Crop image to area we need
            im_crop = im_crop.resize((162,92),resample=Image.NEAREST)
            paint = ""
            for pixel in im_crop.getdata():
                pixel = nearest_colour(palette,pixel) # Get the clostest colour to the pixel in the palette
                if pixel != (255,255,255):
                    paint += hex(colorlen+palette.index(pixel))[2] # Convert to hex
                else:
                    paint += "0" # white
            # Encode paint
            paint = codecs.decode(paint,"hex_codec") # to bytes
            paint = zlib.compress(paint) # compress
            paint = base64.b64encode(paint).decode("utf-8") # base 64 encode

            allpaint[f"0_{x}_{y}.paint"] = paint # Set Paint Data

            crop_pos[0] += screen_size[0] # Update crop pos
        crop_pos[0] = 0
        crop_pos[1] += screen_size[1]

    # Now open default save data :) (i don't want to modify user save data especially since this is modifying the paint)

    print("\nCreating Save.")

    with open("default_save") as f: # Perhaps make this an absolute path to the script file ?? (is a good idea to do this)
        save = f.readlines()

    actualsavething = json.loads(save[3])
    for i,color in enumerate(palette):
        print(rgbToDec(*color),color)
        actualsavething["custompaint_"+str(i)] = rgbToDec(*color)
    actualsavething["custom_color_num"] = actualsavething["custom_color_max"] = len(palette)
    save[3] = json.dumps(actualsavething) + "\n" # Set line 4 to all the shit
    save[18] = json.dumps(allpaint) + "\n" # Set line 19 to paint

    with open("_playdata","w+") as f:
        f.writelines(save) # Write.

    print("Done! :)")

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")
