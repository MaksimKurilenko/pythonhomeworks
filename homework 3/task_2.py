def merge_dicts(dict_a, dict_b):
    for key, value_b in dict_b.items():
        if key in dict_a:
            value_a = dict_a[key]
            if type(value_a)==dict or type(value_b)==dict:
                merge_dicts(value_a, value_b)
            else:
                dict_a[key] = value_b
        else:
            dict_a[key] = value_b
    return dict_a

#example
dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dict_a, dict_b)
print(dict_a)