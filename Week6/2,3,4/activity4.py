# 1. Ignore a value using underscore (_)
name, _, city = ("Alex", 25, "Auckland")
print("Name:", name)
print("City:", city)

# 2. Use underscore in a loop when variable is not needed
for _ in range(3):
    print("Hello")

# 3. Store the result of the last expression temporarily
numbers = [10, 20, 30]
_ = sum(numbers)
print("Sum:", _)

# 4. Use underscore in large numbers for readability
big_number = 1_000_000
print("Big Number:", big_number)

# 5. Separate digits in binary values
binary_value = 0b1010_1111
print("Binary Value:", binary_value)