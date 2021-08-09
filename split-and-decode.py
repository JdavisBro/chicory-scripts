import base64

value = "eJztwUENACAMBDAkDAdkCkjm3xsm7sGj7UzW7bCzw2oBAAAAAAAA33sOtiBB"

n = 2

out = base64.b64decode(value).decode("ascii")

print(out)
