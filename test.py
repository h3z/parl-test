import pickle
from parl_baseline.graph import gen_info, branch_info, bus_info, load_info, graph

# 缓存了一个切面，作为样例
obs = pickle.load(open('obs.pkl', 'rb'))

# 图里每个节点接口要求整数表示。 节点实际名字对应关系在 name2id 和 id2name 里。
graph, name2id, id2name = graph.build_graph(obs)

# 不同节点相关特征值在下边这些字典中，按名字索引。
gen = gen_info.static_and_obs(obs)
branch = branch_info.static_and_obs(obs)
bus = bus_info.static_and_obs(obs)
load = load_info.static_and_obs(obs)

# debug 打断点
print(1)
