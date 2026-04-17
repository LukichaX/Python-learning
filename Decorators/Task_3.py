def validate_numbers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                return "invalid input"
        return func(*args)
    return wrapper

@validate_numbers
def add(a,b):
    return a+b

print(add(1, "2"))