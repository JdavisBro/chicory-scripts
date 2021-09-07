import base64
import zlib
import json
import random

from PIL import Image

EXPECTED = 160*90

palette = {1: (4, 255, 196),2: (185, 255, 96),3: (254, 158, 142),4: (118, 144, 255)}
# 1: black, 2: red, 3: green, 4: blue, 5: yellow185, 255, 96

with open("/home/jdavis/.local/share/Steam/steamapps/compatdata/1123450/pfx/drive_c/users/steamuser/Local Settings/Application Data/paintdog/save/_playdata") as f:
    lines = f.readlines()
    allpaint = json.loads(lines[18])["0_-4_2.paint"]
    del lines

allpaint = zlib.decompress(base64.b64decode(allpaint)).hex()

print(len(allpaint)-EXPECTED)

#paint = allpaint[len(allpaint)-EXPECTED:]
paint = allpaint

paintlist = [[]]

for i, v in enumerate(paint):
    paintlist[-1].append(v)
    if (i+1) % 162 == 0:
        paintlist.append([])

if [] in paintlist:
    paintlist.remove([])

with open("out.txt","w+") as f:
    f.write(paint)

im = Image.new("RGB",(162,92),color=(0,0,0))
print(len(paintlist),paintlist[0],paintlist[-1])
imData = list(im.getdata())
i = 0
for colorlist in paintlist:
    for color in colorlist:
        if int(color,base=16) > 0:
            if int(color,base=16) in palette:
                imData[i] = palette[int(color)]
            else:
                random.seed(color)
                imData[i] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                random.seed()
        i += 1

im.putdata(imData)
im.save("out.png")