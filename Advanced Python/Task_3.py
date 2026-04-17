def safe_divide(a, b):
    if b == 0:
        return "error"
    else:
        return a / b

print(safe_divide(5, 0))