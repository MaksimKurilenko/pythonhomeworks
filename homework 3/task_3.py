import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            with open(filename, "a") as f:
                f.write(f"[{now}] {func.__name__} args={args}, kwargs={kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator
