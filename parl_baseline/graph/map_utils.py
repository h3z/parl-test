# _GEN = 1
# _GEN_RE = 2
# _LOAD = 10
# _LOAD_AD = 11
# _LOAD_STO = 12
# _BUS = 100
# _BRANCH = 1000
#
# TOTAL_LEN = 32

empty_feature_dict = {
    # gen
    'gen_p': 0,
    'gen_q': 0,
    'gen_v': 0,
    'gen_status': 0,
    'actual_dispatch': 0,
    'steps_to_close_gen': 0,
    'steps_to_recover_gen': 0,
    'target_dispatch': 0,
    'nextstep_renewable_gen_p_max': 0,
    'curstep_renewable_gen_p_max': 0,

    # load
    'curstep_ld_p': 0,
    'ld_p': 0,
    'ld_q': 0,
    'ld_v': 0,
    'nextstep_ld_p': 0,
    'adjld_p': 0,
    'total_adjld': 0,
    'stoenergy_p': 0,
    'total_stoenergy': 0,

    # bus
    'bus_v': 0,

    # branch
    'a_ex': 0,
    'a_or': 0,
    'p_ex': 0,
    'p_or': 0,
    'q_ex': 0,
    'q_or': 0,
    'rho': 0,
    'steps_to_reconnect_line': 0,
    'v_ex': 0,
    'v_or': 0,
    'count_soft_overflow_steps': 0,
    'line_status': 0,
}


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
