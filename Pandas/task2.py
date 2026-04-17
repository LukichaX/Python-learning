import pandas as pd

pc_sales = {
    "Part": ["GPU", "CPU", "RAM", "GPU", "RAM", "GPU", "CPU"],
    "Brand": ["NVIDIA", "Intel", "Corsair", "NVIDIA", "Kingston", "AMD", "AMD"],
    "Price": [1200, 400, 150, 1100, 140, 900, 350]
}
df = pd.DataFrame(pc_sales)

grouped_parts = df.groupby("Part")["Price"].sum()

filtered_parts = df[df["Price"] > 500]

print(grouped_parts)

