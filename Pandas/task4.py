import numpy as np
import pandas as pd

components = {
    "Part": ["GPU", "GPU", "CPU", "RAM", "CPU", "RAM"],
    "Model": ["RTX 5060 Ti", "RTX 3070", "i5 12600KF", "32GB DDR4", "i9 13900K", "16GB DDR4"],
    "Price": [600, 450, 250, 150, 600, 80]
}
df = pd.DataFrame(components)

grouped = df.groupby("Part")["Price"].agg(["max", "min"])
sorteddf = df.sort_values(by="Price", ascending=True)

print(sorteddf)