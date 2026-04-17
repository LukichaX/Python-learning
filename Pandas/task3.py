import pandas as pd

sales_data = {
    "Category": ["Laptop", "Phone", "Laptop", "Monitor", "Phone", "Monitor"],
    "Brand": ["HP", "iPhone", "Lenovo", "Dell", "Samsung", "LG"],
    "Total_Sales": [4500, 7000, 3800, 1200, 6500, 1100]
}
df = pd.DataFrame(sales_data)

groupedByCategory = df.groupby("Category")["Total_Sales"].mean()

filtered = df[df["Total_Sales"] > 4000]

print(groupedByCategory)