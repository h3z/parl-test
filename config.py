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


WARMUP_STEPS = 300
MEMORY_SIZE = int(1e6)
BATCH_SIZE = 256
GAMMA = 0.99
TAU = 0.005
ACTOR_LR = 3e-4
CRITIC_LR = 3e-4
OBS_DIM = 819
ACT_DIM = 54
NODE_NUM = 659
NODE_FEA_LEN = len(empty_feature_dict)


