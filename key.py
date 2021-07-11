import json

with open("entrances.json") as f:
    entrances = json.load(f)

out = {}

for entrance in entrances:
    eid = entrance["id"]
    entrance.pop("id")
    out[eid] = entrance

with open("entrancesout.json","w+") as f:
    json.dump(out,f)
