from decorators import log_activity


# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "zoo123"


# Decorated login function
# Validates admin username and password
@log_activity

def admin_login(username, password):

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful.")
        return True

    else:
        print("Invalid username or password.")
        return False


# Decorated function for viewing animal records
@log_activity

def view_animals():

    animals = [
        "Lion",
        "Tiger",
        "Elephant",
        "Giraffe",
        "Zebra"
    ]

    print("Zoo Animals:")

    for animal in animals:
        print(f"- {animal}")


# Decorated function for adding animals
@log_activity

def add_animal(animal_name):

    print(f"{animal_name} added to the zoo records.")