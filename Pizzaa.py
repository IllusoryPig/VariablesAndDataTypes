import dataclasses



@dataclasses.dataclass
class Pizza:
    peppers: int
    peperoni: int
    poultry: int


class Shop:
    def add_pepper(self, pizza: Pizza, peppers: int):
        pizza.peppers += peppers
        return pizza

    def add_peperoni(self, pizza: Pizza, peperoni: int):
        pizza.peperoni += peperoni
        return pizza

    def add_poultry(self, pizza: Pizza, poultry: int):
        pizza.poultry += poultry
        return pizza

if __name__ == "__main__":
    PizzaNova = Shop()

    pizza = Pizza(0, 0, 0)
    print(f"\n\t{pizza}")
    pizza = PizzaNova.add_pepper(pizza, 45)
    print(f"\n\t{pizza}")
    pizza = PizzaNova.add_peperoni(pizza, 400)
    print(f"\n\t{pizza}")
    pizza = PizzaNova.add_poultry(pizza, 61)
    print(f"\n\t{pizza}")

    print("We finished making your pizza. Come again to PizzaNova!")