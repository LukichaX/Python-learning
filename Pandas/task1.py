import pandas as pd

data = {
    "Car_Model": ["BMW X5 E53", "Toyota Vitz", "Mercedes C200", "Subaru Impreza"],
    "Repair_Cost": [850, 150, 420, 1200],
    "Status": ["Pending", "Done", "Pending", "Done"]
}

df = pd.DataFrame(data)

filtered_data = df[df["Repair_Cost"] > 500]

print(filtered_data)

