class RAM_Stick:
    def __init__(self, capacity):
        self.capacity = capacity

    def __add__(self, other):
        return self.capacity + other.capacity


kingston_16gb = RAM_Stick(16)
corsair_8gb = RAM_Stick(8)

total_memory = kingston_16gb + corsair_8gb
print(total_memory)

