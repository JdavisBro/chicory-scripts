import json

with open("levels.json") as f:
    levels = json.load(f)

blank = r"eJztzDEBAAAMAqAKs3\/ZlfATApB0XfkTCoVCoVAoFAqFQqFQKBQKhUKhUCgUCoWT4QNqf+kw"

out = {}

out = {level: blank for level in levels}

with open("out.json","w+") as f:
    json.dump(out,f)

# THIS
# MIGHT
# NOT
# WORK
# CURRENTLY!
