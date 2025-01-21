import json

def load_json(path):
    with open(path)as f:
        return json.load(f)
    
def save_json(obj, save_path, indent=2, **kwargs):
    with open(save_path, 'w+')as f:
        json.dump(obj, f, indent=indent, **kwargs)

def update_json(path, key, new_value, check_key_exist=True, indent=2, **kwargs):
    data = load_json(path)
    if check_key_exist and key not in new_value:
        raise IndexError(f'There is no key named "{key}" in json data ({path}).')
    else:
        data[key] = new_value
        save_json(data, path, indent=indent, **kwargs)