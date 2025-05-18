def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, expected) in enumerate(zip(args, expected_types), start=1):
                if not isinstance(arg, expected):
                    raise TypeError(
                        f"Arg{i} = {arg!r} should be {expected.__name__}, not {type(arg).__name__}"
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator
