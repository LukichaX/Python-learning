class PC:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    def show_specs(self):
        return print(f"ჩემი კომპიუტერის მონაცემებია: {self.cpu} და {self.gpu}")

my_pc = PC("I5-12600KF", "RTX 5060TI 16GB")

my_pc.show_specs()