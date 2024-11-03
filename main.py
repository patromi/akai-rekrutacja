import json
from typing import Dict, List, Any


class Converter:
    CT_TO_OUNCE: float = 0.00705479239
    G_TO_OUNCE: float = 0.0352739619

    def __init__(self):
        self.categories: Dict[str, Dict[str, int]] = self.load_categories("kategorie.json")
        self.data: List[Dict[str, str]] = self.open_json("zbiór_wejściowy.json")
        self.filtered_data: List[Dict[str, Any]] = []

    @staticmethod
    def open_json(file_path: str) -> Dict[str, Any]:
        with open(file_path) as f:
            return json.load(f)

    def load_categories(self, file_path: str) -> Dict[str, Dict[str, int]]:
        categories = self.open_json(file_path)
        category_dict: Dict[str, Dict[str, int]] = {}

        for item in categories:
            item_type: str = item["Typ"]
            purity: str = item["Czystość"]
            unit_price: int = item['Wartość za uncję (USD)']
            if item_type not in category_dict:
                category_dict[item_type] = {}
            category_dict[item_type][purity] = unit_price

        return category_dict

    def calc_oz(self, masa: str) -> float:
        masa = masa.replace(",", ".")
        if masa.endswith("ct"):
            return float(masa[:-2]) * self.CT_TO_OUNCE
        elif masa.endswith("g"):
            return float(masa[:-1]) * self.G_TO_OUNCE
        else:
            raise ValueError(f"Unknown unit: {masa}")

    def map_items(self) -> None:
        for item in self.data:
            purity: str = item.get("Czystość", "")
            name: str = item.get("Typ", "")
            unit_price: int = self.categories.get(name, {}).get(purity, 0)

            if unit_price:
                item["Cena"] = self.calc_oz(item["Masa"]) * unit_price
                self.filtered_data.append(item)

    def get_top_prices(self, top_n: int = 5) -> List[Dict[str, Any]]:
        return sorted(self.filtered_data, key=lambda x: x["Cena"], reverse=True)[:top_n]


def pretty_print(items: List[Dict[str, Any]], fields: List[str]) -> None:
    for item in items:
        for field in fields:
            print(f"{field}: {item[field]}")
        print("###################")


converter = Converter()
converter.map_items()

top_prices = converter.get_top_prices()
pretty_print(top_prices, ["Typ", "Właściciel", "Czystość", "Cena"])
