pc_specs = {
    "GPU": "RTX 5060 Ti",
    "CPU": "i5 12600KF",
    "RAM": "32GB"
}

def get_part(part_name):
    try:
        return  pc_specs[part_name]
    except KeyError:
        return "ნაწილი ვერ მოიძებნა!"
    except Exception as e:
        return f"მოხდა შეცდომა: {e}"


part = input("რა ნაწილი გაინტერესებთ?")

print(get_part(part))