import json

with open("kategorie.json") as cat:
    cat = json.loads(cat.read())

with open("zbiór_wejściowy.json") as data:
    data = json.loads(data.read())

# zamiana masy na uncje

for i in range(len(data)):
    masa = data[i]["Masa"]
    masa = masa.replace(",", ".")
    if masa[-1] == "t":
        masa = float(masa[:-2])/141.7
    else:
        masa = float(masa[:-1])/28.35
    print(masa)