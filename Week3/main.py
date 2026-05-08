from rectangle import Rectangle

def main():
    print("=== Land Area & Perimeter Calculator ===")

    try:
        length = float(input("Enter length of land in metres: "))
        width = float(input("Enter width of land in metres: "))

        if length <= 0 or width <= 0:
            print("Error: Dimensions must be greater than 0")
            return

        land = Rectangle(length, width)
        land.display_info()

    except ValueError:
        print("Error: Please enter valid numbers only")

if __name__ == "__main__":
    main()