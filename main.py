import json

with open("kategorie.json") as kat:
    kat = json.loads(kat.read())

with open("zbiór_wejściowy.json") as data:
    data = json.loads(data.read())

print(type(data[2]))

