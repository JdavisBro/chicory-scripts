layer = 0

topLeft = [-6,-4]

bottomRight = [-4,4]

screens = ""

for x in range(topLeft[0],bottomRight[0]+1):
    for y in range(topLeft[1],bottomRight[1]+1):
        screens += f"{layer}_{x}_{y}\n"

with open("screenShotScreens.txt","w+") as f:
    f.write(screens)
