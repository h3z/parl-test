def obs_map_to(obs, attrs, name2id):
    r = {}
    for attr in attrs:
        array = obs.__getattribute__(attr)
        r[attr] = {k: array[v] for k, v in name2id.items()}
    return r


def map_to(array, name2id):
    return {k: array[v] for k, v in name2id.items()}
