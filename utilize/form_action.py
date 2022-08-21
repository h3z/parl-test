def split_action(action):
    # action[54:]= 0
    p_action = action[:54]
    v_action = action[54:108]
    ld_p_action = action[108:118]
    store_action = action[118:]
    return p_action,v_action,ld_p_action,store_action

def form_action(adjust_gen_p, adjust_gen_v, adjust_adjld_p, adjust_stoenergy_p):
    return {
        'adjust_gen_p': adjust_gen_p,
        'adjust_gen_v': adjust_gen_v,
        'adjust_adjld_p': adjust_adjld_p,
        'adjust_stoenergy_p': adjust_stoenergy_p
    }
