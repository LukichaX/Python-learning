def check_positive(func):
    def wrapper(x):
        if x < 0:
            return "negative not allowed"
        return func(x)
    return wrapper

@check_positive
def square(x):
    return x * x

print(square(5))
print(square(-3))