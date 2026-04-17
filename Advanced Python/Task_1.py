def multiply_by(x):
    def inner(y):
        return x * y
    return inner

f = multiply_by(5)
print(f(3))