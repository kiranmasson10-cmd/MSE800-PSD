from factory import FishFactory
from aquarium import Aquarium


def main():

    aquarium = Aquarium()

    while True:

        print("\nAvailable Fish Types:")
        print("Goldfish, Shark, Angelfish, Tuna, Salmon")

        fish_name = input("Enter fish type (or 'exit' to quit): ")

        if fish_name.lower() == "exit":
            break

        fish = FishFactory.create_fish(fish_name)

        if fish:
            aquarium.add_fish(fish)
            print(f"{fish.category()} added successfully.")
        else:
            print("Invalid fish type.")

    aquarium.display_inventory()


if __name__ == "__main__":
    main()