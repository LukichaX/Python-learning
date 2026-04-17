from collections import Counter

products = ["HP", "Lenovo", "HP", "MSI"]

counter = Counter(products)

for key, value in counter.items():
    print(key, value)
