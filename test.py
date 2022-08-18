import pickle

import example

from parl_baseline.graph import gen_info, branch_info, bus_info, load_info

grid = example.Print()
obs = pickle.load(open('obs.pkl', 'rb'))

gen = gen_info.static_and_obs(obs)
branch = branch_info.static_and_obs(obs)
bus = bus_info.static_and_obs(obs)
load = load_info.static_and_obs(obs)
print(1)
