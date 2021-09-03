import json

with open("/home/jdavis/.local/share/Steam/steamapps/common/Chicory A Colorful Tale/PC/level_data") as f:
    level_data = json.load(f)

animals = {}

for i in level_data.keys():
    if "objects" in level_data[i].keys():
        for o in level_data[i]["objects"]:
            if o["obj"] == "objLost_animal":
                x = o["x"]
                y = o["y"]
                if "attached_object" in o:
                    print(o)
                    attached = [ob for ob in level_data[i]["objects"] if ob.get('id',"n") == o['attached_object']]
                    if attached:
                        x = attached[0]["x"]
                        y = attached[0]["y"]
                animals[f"found_animal_{i}"] = {"x":x,"y":y,"screen":i}

with open("animals.json","w+") as f:
    json.dump(animals,f,indent=4,sort_keys=True)
