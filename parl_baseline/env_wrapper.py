
import gym
import numpy as np
from parl.utils import logger

from Environment.base_env import Environment
from utilize.form_action import *
from utilize.settings import settings
from parl_baseline.graph.graph import Graph

graph = Graph()
class MaxTimestepWrapper(gym.Wrapper):
    def __init__(self, env, max_timestep=288):
        logger.info("[env type]:{}".format(type(env)))
        self.max_timestep = max_timestep
        env.observation_space = None
        env.reward_range = None
        env.metadata = None
        gym.Wrapper.__init__(self, env)

        self.timestep = 0

    def step(self, action, **kwargs):
        self.timestep += 1
        obs, reward, done, info = self.env.step(action, **kwargs)
        if self.timestep >= self.max_timestep:
            done = True
            info["timeout"] = True
        else:
            info["timeout"] = False
        return obs, reward, done, info

    def reset(self, **kwargs):
        self.timestep = 0
        return self.env.reset(**kwargs)


class ObsTransformerWrapper(gym.Wrapper):
    def __init__(self, env):
        logger.info("[env type]:{}".format(type(env)))
        gym.Wrapper.__init__(self, env)

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
        action_space_low[settings.balanced_id] = 0.0
        action_space_high[settings.balanced_id] = 0.0

        features = np.concatenate([
            loads, prods,
            rho.tolist(), next_load, action_space_low, action_space_high
        ])

        # return {'ori_features': features, 'obs': obs}
        return graph.get_features(obs).reshape(-1)

    def step(self, action, **kwargs):
        self.raw_obs, reward, done, info = self.env.step(action, **kwargs)
        obs = self._get_obs(self.raw_obs)
        return obs, reward, done, info

    def reset(self, **kwargs):
        self.raw_obs = self.env.reset(**kwargs)
        obs = self._get_obs(self.raw_obs)
        return obs


class RewardShapingWrapper(gym.Wrapper):
    def __init__(self, env):
        logger.info("[env type]:{}".format(type(env)))
        gym.Wrapper.__init__(self, env)

    def step(self, action, **kwargs):
        obs, reward, done, info = self.env.step(action, **kwargs)

        shaping_reward = 1.0

        info["origin_reward"] = reward

        return obs, shaping_reward, done, info

    def reset(self, **kwargs):
        return self.env.reset(**kwargs)



class ActionWrapper(gym.Wrapper):
    def __init__(self, env, raw_env):
        logger.info("[env type]:{}".format(type(env)))
        gym.Wrapper.__init__(self, env)
        self.raw_env = raw_env
        self.v_action = np.zeros(self.raw_env.settings.gen_num)
        self.ld_p_action = np.zeros(10)
        self.store_action = np.zeros(5)

    def step(self, action, **kwargs):
        p_action,v_action,ld_p_action,store_action = split_action(action)

        p_action = self.post_process(p_action, 'adjust_gen_p', True)
        v_action = self.post_process(v_action, 'adjust_gen_v', True)
        ld_p_action = self.post_process(ld_p_action, 'adjust_adjld_p')
        store_action = self.post_process(store_action, 'adjust_stoenergy_p')
        ret_action = form_action(p_action, v_action, ld_p_action, store_action)
        return self.env.step(ret_action, **kwargs)

    def reset(self, **kwargs):
        return self.env.reset(**kwargs)
    def post_process(self,action, k, is_gen=False):
        gen_p_action_space = self.env.raw_obs.action_space[k]

        low_bound = gen_p_action_space.low
        high_bound = gen_p_action_space.high

        mapped_action = low_bound + (action - (-1.0)) * (
                (high_bound - low_bound) / 2.0)
        if is_gen:
            mapped_action[self.raw_env.settings.balanced_id] = 0.0
        mapped_action = np.clip(mapped_action, low_bound, high_bound)
        return mapped_action


def get_env():
    env = Environment(settings, "EPRIReward")
    env.action_space = None
    raw_env = env

    env = MaxTimestepWrapper(env)
    env = RewardShapingWrapper(env)
    env = ObsTransformerWrapper(env)
    env = ActionWrapper(env, raw_env)

    return env
