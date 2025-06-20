# Recursively flattens a nested dictionary into a single dict, NOTE: dict keys need to be str 
def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            items.append((new_key + '.length', len(v)))
            for i, elem in enumerate(v):
                if isinstance(elem, dict):
                    items.extend(flatten_dict(elem, f"{new_key}.{i}", sep=sep).items())
                else:
                    items.append((f"{new_key}.{i}", elem))
        else:
            items.append((new_key, v))
    return dict(items)