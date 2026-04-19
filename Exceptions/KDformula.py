def calculate_kd(kills, deaths):
    try:
        return kills / deaths
    except ZeroDivisionError:
        return float(kills)
    except Exception as e:
        return f"მოხდა შეცდომა: {e}"

kill = int(input("რამდენი მოთამაშე მოკალით?"))
death = int(input("რამდენჯერ მოკვდით?"))

print(calculate_kd(kill, death))