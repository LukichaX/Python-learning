from collections import defaultdict

orders = [
    ("BMW X5 E53", "O2 Sensor"), 
    ("Toyota Vitz", "Air Filter"), 
    ("BMW X5 E53", "Headlight Cover"), 
    ("Mercedes C200", "Spark Plug"),
    ("Toyota Vitz", "Brake Pads")
]

orders_list=defaultdict(list)

for car, part in orders:
    orders_list[car].append(part)

print(dict(orders_list))