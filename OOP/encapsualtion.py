class CryptoWallet:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
       self.__balance = amount


lukicha = CryptoWallet("Lukicha")

print(lukicha.balance)
lukicha.balance = 50
print(lukicha.balance)