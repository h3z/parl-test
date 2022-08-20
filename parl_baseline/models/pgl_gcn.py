import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import parl
import pgl
from config import BATCH_SIZE, NODE_NUM, NODE_FEA_LEN
from pgl.nn import GCNConv
import numpy as np
from parl_baseline.graph.graph import Graph
from config import NODE_NUM
# clamp bounds for Std of action_log
LOG_SIG_MAX = 2.0
LOG_SIG_MIN = -20.0


class GCNModel(parl.Model):
    def __init__(self, obs_dim, action_dim):
        super(GCNModel, self).__init__()
        self.actor_model = Actor(int(obs_dim / NODE_NUM), 32, action_dim)
        self.critic_model = Critic(obs_dim, action_dim)

    def policy(self, obs):
        return self.actor_model(obs)

    def value(self, obs, action):
        return self.critic_model(obs, action)

    def get_actor_params(self):
        return self.actor_model.parameters()

    def get_critic_params(self):
        return self.critic_model.parameters()


class Actor(parl.Model):
    def __init__(self, gcn_in, gen_out, action_dim):
        super(Actor, self).__init__()

        # norm = True 的话 pgl 库会报错，
        self.gcn = GCNConv(gcn_in, gen_out, norm=False)
        self.mean_linear = nn.Linear(NODE_NUM*gen_out, action_dim)
        self.std_linear = nn.Linear(NODE_NUM*gen_out, action_dim)
        self.graph = pgl.Graph.batch([Graph().graph]*BATCH_SIZE)


    def forward(self, obs):
        # features = self.graph.get_features(obs)
        features = paddle.reshape(obs, (-1, NODE_FEA_LEN))
        x = self.gcn(self.graph, features)
        x = paddle.reshape(x, (obs.shape[0], -1))

        act_mean = self.mean_linear(x)
        act_std = self.std_linear(x)
        act_log_std = paddle.clip(act_std, min=LOG_SIG_MIN, max=LOG_SIG_MAX)
        return act_mean, act_log_std


class Critic(parl.Model):
    def __init__(self, obs_dim, action_dim):
        super(Critic, self).__init__()

        # Q1 network
        self.l1 = nn.Linear(obs_dim + action_dim, 512)
        self.l2 = nn.Linear(512, 256)
        self.l3 = nn.Linear(256, 1)

        # Q2 network
        self.l4 = nn.Linear(obs_dim + action_dim, 512)
        self.l5 = nn.Linear(512, 256)
        self.l6 = nn.Linear(256, 1)

    def forward(self, obs, action):
        x = paddle.concat([obs, action], 1)

        # Q1
        q1 = F.relu(self.l1(x))
        q1 = F.relu(self.l2(q1))
        q1 = self.l3(q1)

        # Q2
        q2 = F.relu(self.l4(x))
        q2 = F.relu(self.l5(q2))
        q2 = self.l6(q2)
        return q1, q2
