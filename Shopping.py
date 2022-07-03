import dataclasses


# This is a Data Class. It only holds variables, no methods in it.
# Keeps items.
@dataclasses.dataclass
class Refrigerator:
    number_of_eggs: int
    bottles_of_milk: int
    fruits: int

# This is a Method/Function Class. It only does work.
class SuperMarket:
    def add_eggs(self, refrigerator: Refrigerator, number_of_eggs: int):
        refrigerator.number_of_eggs += number_of_eggs
        return refrigerator

    def add_milk(self, refrigerator: Refrigerator, bottles_of_milk: int):
        refrigerator.bottles_of_milk += bottles_of_milk
        return refrigerator

    def add_fruits(self, refrigerator: Refrigerator, fruits: int):
        refrigerator.fruits += fruits
        return refrigerator


# This is where we go shopping.
if __name__ == "__main__":
    stop_and_shop = SuperMarket()

    refrigerator = Refrigerator(0, 0, 0)
    print(f"\n\t{refrigerator}")
    refrigerator = stop_and_shop.add_eggs(refrigerator, 24)
    print(f"\n\t{refrigerator}")
    refrigerator = stop_and_shop.add_milk(refrigerator, 6)
    print(f"\n\t{refrigerator}")
    refrigerator = stop_and_shop.add_fruits(refrigerator, 49)
    print(f"\n\t\t{refrigerator}")

    print("Shopping Complete. Come to Stop $ Shop again!")

# Harder
    class Refrigerator1:
        def __init__(self, no_of_eggs: int, bottles_of_milk: int, no_of_fruits: int):
            self.number_of_eggs = no_of_eggs
            self.bottles_of_milk = bottles_of_milk
            self.fruits = no_of_fruits

    refrigerator = Refrigerator1(0, 0, 0)



