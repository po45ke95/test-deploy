from collections.abc import MutableMapping

d = {'a': 1,'c': {'a': 2,'b': {'x': 5,'y' : 10}},'d': [1, 2, 3]}

print(type(d))
def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str ='.') -> MutableMapping:
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
print(flatten_dict(d))