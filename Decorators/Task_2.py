import time


def measure_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(end_time - start_time)
        return result
    return wrapper

@measure_time
def custom_function():
    time.sleep(2)
    return 2

print(custom_function())