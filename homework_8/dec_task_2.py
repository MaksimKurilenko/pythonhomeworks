def retry(exception_type, n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except exception_type as e:
                    print(f"[{attempt}/n] Exception: {e}. Retrying...")
                    last_exception = e
                    raise last_exception
            return None

        return wrapper

    return decorator
