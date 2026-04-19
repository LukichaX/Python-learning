class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return F"იარაღი: {self.name}, ზიანი: {self.damage}"


obj1 = Weapon("AK-47", 36)

print(obj1)