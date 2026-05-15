from admin import (
    admin_login,
    view_animals,
    add_animal,
)


# Main controller function

def main():

    print("===== Zoo Admin Login System =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Verify login
    if admin_login(username, password):

        print("\nWelcome Admin!\n")

        # View zoo animals
        view_animals()

        # Add a new animal
        animal = input("\nEnter animal to add: ")
        add_animal(animal)

    else:
        print("Access denied.")


# Program entry point
if __name__ == "__main__":
    main()