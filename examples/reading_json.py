import json

file = open('FMCD.json')

# Use load() to read a file
data = json.load(file)

for i in data['SIMCARR']['wellpath']['trajectoryItem']:
    print(i)
file.close()