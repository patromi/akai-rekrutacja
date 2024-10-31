import json
from prettyprint import prettyprint

with open("kategorie.json") as cat:
    cat = json.loads(cat.read())

with open("zbiór_wejściowy.json") as data:
    data = json.loads(data.read())

# zamiana masy na uncje

for i in range(len(data)):
    masa = data[i]["Masa"]
    masa = masa.replace(",", ".")
    if masa[-1] == "t":
        data[i]["Masa"] = float(masa[:-2])/141.7
    else:
        data[i]["Masa"] = float(masa[:-1])/28.35

# przypisanie ceny

for i in range(len(data)):
    data[i].update({"Cena": 0})
    for j in range(len(cat)):
        if data[i]["Typ"] == cat[j]["Typ"] and data[i]["Czystość"] == cat[j]["Czystość"]:
            data[i]["Cena"] = round(data[i]["Masa"]*cat[j]["Wartość za uncję (USD)"], 2)
            break

# szukanie najwyzszych cen

max = [{"Cena": 0}, {"Cena": 0}, {"Cena": 0}, {"Cena": 0}, {"Cena": 0}]

for i in range(len(data)):
    for j in range(5):
        if data[i]["Cena"] > max[j]["Cena"]:
            max[j] = data[i]
            break

# printowanie odpowiedzi

prettyprint(max, data[0].keys())