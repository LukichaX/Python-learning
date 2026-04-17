numbers = []
print("Input 5 numbers")

for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

print("Sum of all numbers in list: ", sum(numbers))