import json

with open("sortMe.json") as f:
    sortMe = json.load(f)

nameToKey = {}

for key in sortMe.keys():
    nameToKey[sortMe[key]["name"]] = key

sortedMe = {}

for name in sorted(list(nameToKey.keys())):
    sortedMe[nameToKey[name]] = sortMe[nameToKey[name]]

with open("sortedMe.json","w+") as f:
    json.dump(sortedMe,f)
