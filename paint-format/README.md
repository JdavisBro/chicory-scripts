# Paint Format

OK i wanna find out the paint format in the save data!!!
and also the geo format found in level_data (for custom levels!)

## Scripts

py on windows, else python3

[make sure pillow is installed](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)

`py draw_data.py SCREEN`

screen should be something like 0_1_2

LAYER_X_Y
it should find your save and level_data,

if it's in a different place than it normally is add `-h` on the command to get help


## How to

I DID IT I DID IT

> HOW TO GET THE DATA

base64 decode your string

gzip or zlib or whatever decompress that

and turn that into hex

now you have a hex string or something, each character is 1 pixel in a 162 by 92 image, there is a border of 1 pixel around the edges for [marching squares](https://www.yoyogames.com/en/blog/how-painting-works-in-chicory-a-colorful-tale) so to get the displayed square crop it at 1, 1 for 160, 90
