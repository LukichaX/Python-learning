import time
from functools import lru_cache

@lru_cache(maxsize=None)
def get_user_data(user_id):
    print("მონაცემების ჩამოტვირთვა სერვერიდან...")
    time.sleep(3)
    return f"მომხმარებელი: {user_id}"

print(get_user_data(10))
print(get_user_data(10))
print(get_user_data(10))