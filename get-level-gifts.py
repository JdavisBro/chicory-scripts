import json

with open("/home/jdavis/.local/share/Steam/steamapps/common/Chicory A Colorful Tale/PC/level_data") as f:
    level_data = json.load(f)

gifts = {}

for i in level_data.keys():
    if "objects" in level_data[i].keys():
        giftN = 0
        for o in level_data[i]["objects"]:
            if o["obj"] == "objGift":
                giftN += 1
                if giftN > 1:
                    print(f"Gift in {level_data[i]['name']} will be message")
                gifts[f"gift_{o.get('name',level_data[i]['name'])}"] = {"x":o["x"],"y":o["y"],"screen":i}

with open("gifts.json","w+") as f:
    json.dump(gifts,f,indent=4,sort_keys=True)

# WARN: This scripts ignores 3 gifts beucase they are in the same room as another, they're in luncheon, grub deep and supper woods
