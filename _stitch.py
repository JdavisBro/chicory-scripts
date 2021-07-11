import os
from PIL import Image, ImageDraw

files = [f for f  in os.listdir() if not f.startswith("_") and '_' in f]

firstscreen = [int(p) for p in files[0][:-4].split("_")]
lowestx = firstscreen[1]
lowesty = firstscreen[1]
highestx = firstscreen[2]
highesty = firstscreen[2]
for f in files[1:]:
    im_grid_pos = [int(p) for p in f[:-4].split("_")]
    if f[1] < lowestx: lowestx = f[1]
    if f[1] > highestx: highestx = f[1]
    if f[2] < lowesty: lowesty = f[2]
    if f[2] > highesty: highesty = f[2]
xsize = highestx-lowestx
ysize = highesty-lowesty

layer = -1 # -1 means all layers

grid_size_div = 10

grid_size = [1920//grid_size_div,1080//grid_size_div]

centre_pos = [grid_size[0]*xnsize,grid_size[1]*ynsize]

image = Image.new("RGBA",(grid_size[0]*xsize,grid_size[1]*ysize),color=(0,0,0,0))

draw = ImageDraw.Draw(image)

display_grid_pos = False

print(centre_pos)

for f in files:
    im_grid_pos = [int(p) for p in f[:-4].split("_")]
    if im_grid_pos[0] == layer or layer == -1:
        im = Image.open(f)
        im = im.resize(grid_size)
        im_pos = [centre_pos[0]+grid_size[0]*im_grid_pos[1],centre_pos[1]+grid_size[1]*im_grid_pos[2]]
        image.paste(im,im_pos)
        if display_grid_pos:
            draw.text(im_pos[:2],"_".join([str(i) for i in im_grid_pos[1:]]),fill=(255,255,255))
            draw.text((im_pos[0],im_pos[1]+200//grid_size_div),"_".join([str(i) for i in im_grid_pos[1:]]),fill=(0,0,0))

image.save(f"_out{str(layer)}.png")
