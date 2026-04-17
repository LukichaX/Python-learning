students = {
    "Luka": [90,80],
    "Mate": [50, 60]
}

def highest_avg(students):
    score = 0
    name = ""

    for key, value in students.items():
        avg = sum(value) / len(value)
        if avg > score:
            score = avg
            name = key

    return name + ": " + str(score)



print(highest_avg(students))