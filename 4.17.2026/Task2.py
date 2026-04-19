import inspect


def calculate_performance(gpu_clock, vram_size=16):
    """ითვლის გრაფიკული ბარათის სიმძლავრეს"""
    return gpu_clock * vram_size


print(inspect.getsource(calculate_performance()))
