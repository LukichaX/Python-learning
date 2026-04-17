def divide(a, b):
    return a / b

def safe_divide(a, b):
    if b == 0:
        return "error"

    return divide(a, b)

print(safe_divide(10, 2))
print(safe_divide(10, 0))