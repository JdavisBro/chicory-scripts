import os
import json

with open("/home/jdavis/.local/share/Steam/steamapps/common/Chicory A Colorful Tale/PC/level_data") as f:
    level_data = json.load(f)
levels = list(level_data.keys())

# levels = os.listdir("/home/jdavis/.local/share/Steam/steamapps/compatdata/1123450/pfx/drive_c/users/steamuser/Local Settings/Application Data/paintdog/100save/timelapse")

with open("levels.json","w+") as f:
    json.dump(sorted(levels),f)

# for i in level_data.keys():
#     level_data[i]["area"] = "none"

for i in level_data.keys():
    if "objects" in level_data[i].keys():
        for i2, _ in enumerate(level_data[i]["objects"]):
            if "attached_object" in level_data[i]["objects"][i2].keys():
                level_data[i]["objects"][i2].pop("attached_object")
                print(level_data[i]["objects"][i2])

with open("level_data","w+") as f:
    json.dump(level_data,f)
