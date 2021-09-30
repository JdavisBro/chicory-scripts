import json

with open("/home/jdavis/.local/share/Steam/steamapps/common/Chicory A Colorful Tale/PC/level_data") as f:
    level_data = json.load(f)


include = "boss"

for screen, level in level_data.items():
    if "objects" not in level:
        continue
    for obj in level["objects"]:
        if include in obj["obj"].lower():
            print(obj)
