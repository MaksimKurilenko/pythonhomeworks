import time


def rate_limit(max_calls, period_seconds):
    def decorator(func):
        call_times = []

        def wrapper(*args, **kwargs):
            current_time = time.time()
            nonlocal call_times
            call_times = [t for t in call_times if current_time - t < period_seconds]

            if len(call_times) >= max_calls:
                raise RuntimeError(
                    f"Limit {max_calls} exceeded in {period_seconds} seconds"
                )

            call_times.append(current_time)
            return func(*args, **kwargs)

        return wrapper

    return decorator
