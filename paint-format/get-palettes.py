import os
import json

# This script is for getting a list of all palettes ready for filling in with colours.
# All colours will be 255,255,255 by default except the last one which is a screen that uses this palette.

level_data_location = "/home/jdavis/Documents/GitHub/chicory-tools/pGamesFiles/level_data"

with open(level_data_location) as f:
    level_data = json.load(f)

if os.path.exists("palettes.json"):
    with open("palettes.json") as f:
        palettes = json.load(f)
else:
    palettes = {}

print(palettes)

for screen in level_data:
    if "palette" not in level_data[screen]:
        continue
    if level_data[screen]["palette"] == "":
        continue
    location = screen.split("_")
    if level_data[screen]["palette"] not in palettes:
        palettes[level_data[screen]["palette"]] = {}
    if "screens" not in palettes[level_data[screen]["palette"]]:
        palettes[level_data[screen]["palette"]]["screens"] = []
    palettes[level_data[screen]["palette"]]["screens"].append(screen)
    if "colors" not in palettes[level_data[screen]["palette"]]:
        palettes[level_data[screen]["palette"]]["colors"] = ((255,255,255),(255,255,255),(255,255,255),(int(location[0]),int(location[1]),int(location[2])))

with open("palettes.json","w+") as f:
    json.dump(palettes,f,indent=4)
