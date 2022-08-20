from config import empty_feature_dict
# _GEN = 1
# _GEN_RE = 2
# _LOAD = 10
# _LOAD_AD = 11
# _LOAD_STO = 12
# _BUS = 100
# _BRANCH = 1000
#
# TOTAL_LEN = 32



def feature_padding(feature_dict):
    empty_feature_dict.update(feature_dict)
    return list(empty_feature_dict.values())


def obs_map_to(obs, attrs, name2id):
    r = {}
    for attr in attrs:
        array = obs.__getattribute__(attr)
        r[attr] = {k: array[v] for k, v in name2id.items()}
    return r


def map_to(array, name2id):
    return {k: array[v] for k, v in name2id.items()}
