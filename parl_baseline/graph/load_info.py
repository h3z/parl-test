from parl_baseline.graph.map_utils import *

adjld_a = [0.069663, 0.069663, 0.069663, 0.069663, 0.069663, 0.069663, 0.069663, 0.069663, 0.069663, 0.069663]
adjld_b = [37.6968, 37.6968, 37.6968, 37.6968, 37.6968, 37.6968, 37.6968, 37.6968, 37.6968, 37.6968]
adjld_c = [31.67, 31.67, 31.67, 31.67, 31.67, 31.67, 31.67, 31.67, 31.67, 31.67]
adjld_capacity = [15.0, 15.0, 25.0, 25.0, 32.0, 32.0, 30.0, 30.0, 24.0, 25.0]
adjld_uprate = [3.0, 5.0, 5.0, 5.0, 4.0, 4.0, 10.0, 10.0, 3.0, 5.0]
adjld_dnrate = [3.0, 5.0, 5.0, 5.0, 4.0, 4.0, 10.0, 10.0, 3.0, 5.0]
stoenergy_k = [1, 1, 1, 1, 1]
stoenergy_b = [1, 1, 1, 1, 1]
stoenergy_name = ['bus.1.ld', 'bus.16.ld', 'bus.23.ld', 'bus.53.ld', 'bus.114.ld']
stoenergy_capacity = [10.0, 10.0, 15.0, 15.0, 10.0]
stoenergy_chargerate_max = [3.0, 3.0, 5.0, 5.0, 3.0]
stoenergy_dischargerate_max = [2.0, 2.0, 3.0, 3.0, 2.0]

# 2 是储能，5个。1 是可调，10个。0 是普通，76 个。
ld_type = [2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0,
           0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
           0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]
ld_name = ['bus.1.ld', 'bus.2.ld', 'bus.3.ld', 'bus.4.ld', 'bus.6.ld', 'bus.7.ld', 'bus.11.ld',
           'bus.12.ld', 'bus.13.ld', 'bus.14.ld', 'bus.15.ld', 'bus.16.ld', 'bus.17.ld', 'bus.18.ld', 'bus.19.ld',
           'bus.20.ld', 'bus.21.ld', 'bus.22.ld', 'bus.23.ld', 'bus.27.ld', 'bus.28.ld', 'bus.29.ld', 'bus.31.ld',
           'bus.32.ld', 'bus.33.ld', 'bus.34.ld', 'bus.35.ld', 'bus.36.ld', 'bus.39.ld', 'bus.40.ld', 'bus.41.ld',
           'bus.42.ld', 'bus.43.ld', 'bus.44.ld', 'bus.45.ld', 'bus.46.ld', 'bus.47.ld', 'bus.48.ld', 'bus.49.ld',
           'bus.50.ld', 'bus.51.ld', 'bus.52.ld', 'bus.53.ld', 'bus.54.ld', 'bus.55.ld', 'bus.56.ld', 'bus.57.ld',
           'bus.58.ld', 'bus.59.ld', 'bus.60.ld', 'bus.62.ld', 'bus.66.ld', 'bus.67.ld', 'bus.70.ld', 'bus.74.ld',
           'bus.75.ld', 'bus.76.ld', 'bus.77.ld', 'bus.78.ld', 'bus.79.ld', 'bus.80.ld', 'bus.82.ld', 'bus.83.ld',
           'bus.84.ld', 'bus.85.ld', 'bus.86.ld', 'bus.88.ld', 'bus.90.ld', 'bus.92.ld', 'bus.93.ld', 'bus.94.ld',
           'bus.95.ld', 'bus.96.ld', 'bus.97.ld', 'bus.98.ld', 'bus.100.ld', 'bus.101.ld', 'bus.102.ld',
           'bus.103.ld', 'bus.104.ld', 'bus.105.ld', 'bus.106.ld', 'bus.107.ld', 'bus.108.ld', 'bus.109.ld',
           'bus.110.ld', 'bus.112.ld', 'bus.114.ld', 'bus.115.ld', 'bus.117.ld', 'bus.118.ld']
ad_ld_name = [name for i, name in enumerate(ld_name) if ld_type[i] == 1]
sto_energy_ld_name = [name for i, name in enumerate(ld_name) if ld_type[i] == 2]

obs_load_name2id = {name: i for i, name in enumerate(ld_name)}
obs_ad_load_name2id = {name: i for i, name in enumerate(ad_ld_name)}
obs_sto_energy_load_name2id = {name: i for i, name in enumerate(sto_energy_ld_name)}


def static_and_obs(obs):
    assert (len(ld_name) == 91)
    assert (len(ad_ld_name) == 10)
    assert (len(sto_energy_ld_name) == 5)

    ad_ld_from_obs = obs_map_to(obs, ['adjld_p', 'total_adjld'], obs_ad_load_name2id)
    sto_energy_from_obs = obs_map_to(obs, ['stoenergy_p', 'total_stoenergy'], obs_sto_energy_load_name2id)
    from_obs = obs_map_to(obs, ['curstep_ld_p', 'ld_p', 'ld_q', 'ld_v', 'nextstep_ld_p'], obs_load_name2id)

    from_obs.update(ad_ld_from_obs)
    from_obs.update(sto_energy_from_obs)
    return {
        'obs': from_obs,
        'static': {
            'ld_type': map_to(ld_type, obs_load_name2id),
            'adjld_a': map_to(adjld_a, obs_ad_load_name2id),
            'adjld_b': map_to(adjld_b, obs_ad_load_name2id),
            'adjld_c': map_to(adjld_c, obs_ad_load_name2id),
            'adjld_capacity': map_to(adjld_capacity, obs_ad_load_name2id),
            'adjld_uprate': map_to(adjld_uprate, obs_ad_load_name2id),
            'adjld_dnrate': map_to(adjld_dnrate, obs_ad_load_name2id),
            'stoenergy_k': map_to(stoenergy_k, obs_sto_energy_load_name2id),
            'stoenergy_b': map_to(stoenergy_b, obs_sto_energy_load_name2id),
            'stoenergy_name': map_to(stoenergy_name, obs_sto_energy_load_name2id),
            'stoenergy_capacity': map_to(stoenergy_capacity, obs_sto_energy_load_name2id),
            'stoenergy_chargerate_max': map_to(stoenergy_chargerate_max, obs_sto_energy_load_name2id),
            'stoenergy_dischargerate_max': map_to(stoenergy_dischargerate_max, obs_sto_energy_load_name2id),
        }
    }
