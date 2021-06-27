import json

with open("/home/jdavis/.local/share/Steam/steamapps/compatdata/1123450/pfx/drive_c/users/steamuser/Local Settings/Application Data/paintdog/save/_playdata","r") as f:
    lines = f.readlines()

save = json.loads(lines[3])
del lines

litter = []
gifts = []
stamps = []

for i in save.keys():
    if "litter" in i:
        litter.append(i)
    elif "gift" in i:
        gifts.append(i)
    elif "stamp" in i:
        stamps.append(i)

with open("save_litter.json","w+") as f:
    json.dump(litter,f,indent=4,sort_keys=True)

with open("save_gift.json","w+") as f:
    json.dump(gifts,f,indent=4,sort_keys=True)

with open("save_stamp.json","w+") as f:
    json.dump(sorted(stamps),f,indent=4,sort_keys=True)
