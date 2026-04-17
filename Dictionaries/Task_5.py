students = {
    "Luka": [90, 85, 88],
    "Nika": [70, 75, 80]
}

for key, value in students.items():
    avg = sum(value) / len(value)
    print(key, avg)