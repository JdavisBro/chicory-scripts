import os
import json

# This script gets a list of levels included in the level_data file which will be all used maps.
# This is used to generate a list of levels to take screnshots

LEVEL_DATA_PATH = "/home/jdavis/.local/share/Steam/steamapps/common/Chicory A Colorful Tale/PC/level_data"

with open(LEVEL_DATA_PATH) as f:
    level_data = json.load(f)
levels = list(level_data.keys())

with open("levels.json","w+") as f:
    json.dump(sorted(levels),f)

# MODIFY LEVEL DATA:

#for i in level_data.keys():
#    level_data[i]["area"] = "none"

#for i in level_data.keys():
#    if "objects" in level_data[i].keys():
#        for i2, _ in enumerate(level_data[i]["objects"]):
#            if "attached_object" in level_data[i]["objects"][i2].keys():
#                level_data[i]["objects"][i2].pop("attached_object")

#with open("level_data","w+") as f:
#    json.dump(level_data,f)
