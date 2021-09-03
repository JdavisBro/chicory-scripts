import os
import sys
from PIL import Image, ImageDraw

if len(sys.argv) == 1:
    print("Required layer argument missing. Layer can be -1 for who cares or 0, 1, 2.")
    sys.exit()
else:
    try:
        layer = int(sys.argv[1])
    except ValueError:
        print("Layer argument invalid, must be a number between -1 and 2")
        sys.exit()

files = [(f,f[:-4].split("_")) for f in os.listdir() if not f.startswith("_") and '_' in f]
files = [(f[0],[int(p) for p in f[1]]) for f in files if int(f[1][0]) == layer or layer == -1]

lowestx = files[0][1][1]
lowesty = files[0][1][1]
highestx = files[0][1][2]
highesty = files[0][1][2]
for _,f in files[1:]:
    if f[1] < lowestx: lowestx = f[1]
    if f[1] > highestx: highestx = f[1]
    if f[2] < lowesty: lowesty = f[2]
    if f[2] > highesty: highesty = f[2]
xsize = highestx-lowestx
ysize = highesty-lowesty

grid_size_div = 10

grid_size = [1920//grid_size_div,1080//grid_size_div]

centre_pos = [grid_size[0]*-lowestx,grid_size[1]*-lowesty]

image = Image.new("RGBA",(grid_size[0]*xsize,grid_size[1]*ysize),color=(0,0,0,0))

draw = ImageDraw.Draw(image)

display_grid_pos = False

print(centre_pos)

for f,im_grid_pos in files:
    im = Image.open(f)
    im = im.resize(grid_size)
    im_pos = [centre_pos[0]+grid_size[0]*im_grid_pos[1],centre_pos[1]+grid_size[1]*im_grid_pos[2]]
    image.paste(im,im_pos)
    if display_grid_pos:
        draw.text(im_pos[:2],"_".join([str(i) for i in im_grid_pos[1:]]),fill=(255,255,255))
        draw.text((im_pos[0],im_pos[1]+200//grid_size_div),"_".join([str(i) for i in im_grid_pos[1:]]),fill=(0,0,0))

image.save(f"_out{str(layer)}.png")
