import time


def warn_if_slow(threshold=1.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            if duration > threshold:
                print(f"Warning! {func.__name__}' running {duration:.2f} sec")
            return result

        return wrapper

    return decorator
