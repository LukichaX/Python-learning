class GPU:
    def __init__(self, model):
        self.model = model
        self.__temperature = 40

    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, value):
        if value > 105:
            return print("კრიტიკული შეცდომა: ტემპერატურა ძალიან მაღალია! სისტემა ითიშება.")
        else:
            self.__temperature = value

myGPU = GPU("RTX 5060TI 16GB")
print(myGPU.temperature)
myGPU.temperature = 106
print(myGPU.temperature)

print(myGPU.temperature(106))