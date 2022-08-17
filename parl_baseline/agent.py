import numpy as np
from parl.algorithms import SAC

from parl_baseline.grid_agent import GridAgent
from parl_baseline.grid_model import GridModel

OBS_DIM = 819
ACT_DIM = 54
GAMMA = 0.99
TAU = 0.005
ACTOR_LR = 3e-4
CRITIC_LR = 3e-4
ALPHA = 0.2
from abc import abstractmethod


class BaseAgent():
    def __init__(self, settings):
        self.settings = settings

    def reset(self, ons):
        pass

    @abstractmethod
    def act(self, obs, reward, done=False):
        pass


class Agent(BaseAgent):

    def __init__(self, settings, this_directory_path=None, seed=None):
        BaseAgent.__init__(self, settings)
        self.seed = seed
        self.settings = settings

        model = GridModel(OBS_DIM, ACT_DIM)
        algorithm = SAC(
            model,
            gamma=GAMMA,
            tau=TAU,
            alpha=ALPHA,
            actor_lr=ACTOR_LR,
            critic_lr=CRITIC_LR)
        self.agent = GridAgent(algorithm)
        self.agent.restore(f"{this_directory_path}/model")

        self.v_action = np.zeros(self.settings.gen_num)
        self.ld_p_action = np.zeros(10)
        self.store_action = np.zeros(5)

    def act(self, raw_obs, reward=0.0, done=False):
        obs = self._get_obs(raw_obs)
        adjust_gen_p = self.agent.predict(obs)

        gen_p_action_space = raw_obs.action_space['adjust_gen_p']

        low_bound = gen_p_action_space.low
        high_bound = gen_p_action_space.high

        mapped_action = low_bound + (adjust_gen_p - (-1.0)) * (
                (high_bound - low_bound) / 2.0)
        mapped_action[self.settings.balanced_id] = 0.0
        mapped_action = np.clip(mapped_action, low_bound, high_bound)

        return form_action(mapped_action, self.v_action, self.ld_p_action, self.store_action)

    def _get_obs(self, obs):
        # loads
        loads = []
        loads.append(obs.ld_p)
        loads.append(obs.ld_q)
        loads.append(obs.ld_v)
        loads = np.concatenate(loads)

        # prods
        prods = []
        prods.append(obs.gen_p)
        prods.append(obs.gen_q)
        prods.append(obs.gen_v)
        prods = np.concatenate(prods)

        # rho
        rho = np.array(obs.rho) - 1.0

        next_load = obs.nextstep_ld_p

        # action_space
        action_space_low = obs.action_space['adjust_gen_p'].low.tolist()
        action_space_high = obs.action_space['adjust_gen_p'].high.tolist()
        action_space_low[self.settings.balanced_id] = 0.0
        action_space_high[self.settings.balanced_id] = 0.0

        features = np.concatenate([
            loads, prods,
            rho.tolist(), next_load, action_space_low, action_space_high
        ])

        return features


def form_action(adjust_gen_p, adjust_gen_v, adjust_adjld_p, adjust_stoenergy_p):
    return {
        'adjust_gen_p': adjust_gen_p,
        'adjust_gen_v': adjust_gen_v,
        'adjust_adjld_p': adjust_adjld_p,
        'adjust_stoenergy_p': adjust_stoenergy_p
    }
