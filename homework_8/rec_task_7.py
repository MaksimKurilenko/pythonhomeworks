def serialize(obj):
    if isinstance(obj, str):

        escaped = obj.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'

    elif isinstance(obj, list):

        serialized_items = [serialize(item) for item in obj]
        return "[" + ", ".join(serialized_items) + "]"

    elif isinstance(obj, dict):

        items = []
        for key, value in obj.items():
            if not isinstance(key, str):
                raise TypeError("Keys must be strings")
            items.append(f"{serialize(key)}: {serialize(value)}")
        return "{" + ", ".join(items) + "}"

    elif isinstance(obj, (int, float, bool)) or obj is None:

        return str(obj).lower() if isinstance(obj, bool) or obj is None else str(obj)

    else:
        raise TypeError(f"Type {type(obj)} is not supported")
