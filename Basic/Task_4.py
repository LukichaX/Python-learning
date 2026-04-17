numbers = []

print("Input 5 numbers")

for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

print(f"Your Numbers: ", numbers)

print("Max: ", max(numbers))
print("Min: ", min(numbers))