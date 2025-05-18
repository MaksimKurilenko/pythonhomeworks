import time


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration_ms = (end_time - start_time) * 1000
        print(f"Function runtime: {func.__name__}: {duration_ms}ms")
        return result

    return wrapper
