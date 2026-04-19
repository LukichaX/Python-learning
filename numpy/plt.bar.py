import matplotlib.pyplot as plt
import numpy as np

names = ["RTX 3070", "RTX 4060 Ti", "RTX 5060 Ti"]
prices = [450, 600, 800]

plt.bar(names,prices)
plt.show()