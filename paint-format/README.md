# Paint Format

OK i wanna find out the paint format in the save data!!!
and also the geo format found in level_data (for custom levels!)

## What we know

I DID IT I DID IT

> HOW TO GET THE DATA

base64 decode your string

gzip (i think) decompress that

and turn that into hex

now you have a hex string or something, each character is 1 pixel in a 162 by 92 image, there is a border of 1 pixel around the edges for [marching squares](https://www.yoyogames.com/en/blog/how-painting-works-in-chicory-a-colorful-tale) so to get the displayed square crop it at 1,1 for 160,90 