class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def cast_spell(self):
        if self.mana < 10:
            return f"mana is less than 10, cant use spell!"
        else:
            self.mana = self.mana - 10
            return f"ჯადოქრობა გამოყენებულია! დარჩენილი მანა: {self.mana}"

witch = Mage("Witch", 100, 50)

for i in range(6):
    print(witch.cast_spell())
