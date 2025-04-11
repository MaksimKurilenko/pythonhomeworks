def cache_func (func):
    cache = {}
    def wrapper (*args, **kwargs):
        key = (args, str(kwargs))
        if key in cache:
            return(cache[key])
        result = func(*args,**kwargs)
        cache[key] = result
        return result
    return wrapper