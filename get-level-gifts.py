import json

with open("/home/jdavis/.local/share/Steam/steamapps/common/Chicory A Colorful Tale/PC/level_data") as f:
    level_data = json.load(f)

litter = {}

for i in level_data.keys():
    if "objects" in level_data[i].keys():
        for o in level_data[i]["objects"]:
            if o["obj"] == "objLitter":
                litter[f"found_litter_{level_data[i]['name']}_{int(o['x'])}_{int(o['y'])}"] = {"x":o["x"],"y":o["y"],"screen":i}

with open("litter.json","w+") as f:
    json.dump(litter,f,indent=4,sort_keys=True)
