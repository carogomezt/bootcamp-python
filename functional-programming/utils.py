from functools import wraps
import time


def log_step(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Running: {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[LOG] Completed: {func.__name__} in {end - start:.2f}s")
        return result
    return wrapper
