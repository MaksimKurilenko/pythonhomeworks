def to_camel_case(s):
    parts = s.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


def to_camel_case_keys(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = to_camel_case(key)
            new_dict[new_key] = to_camel_case_keys(value)
        return new_dict
    elif isinstance(data, list):
        return [to_camel_case_keys(item) for item in data]
    else:
        return data
