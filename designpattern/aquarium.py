class Aquarium:

    __instance = None

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = super(Aquarium, cls).__new__(cls)
            cls.__instance.inventory = {}

        return cls.__instance

    def add_fish(self, fish):

        category = fish.category()

        if category in self.inventory:
            self.inventory[category] += 1
        else:
            self.inventory[category] = 1

    def display_inventory(self):

        print("\nAquarium Fish Inventory")
        print("-" * 30)

        for fish, count in self.inventory.items():
            print(f"{fish}: {count}")
