
import numpy as np
import paddle
import parl


class GridAgent(parl.Agent):
    def __init__(self, algorithm):
        super(GridAgent, self).__init__(algorithm)

        self.alg.sync_target(decay=0)

    def predict(self, obs):
        obs = paddle.to_tensor(obs.reshape(1, -1), dtype='float32')
        action = self.alg.predict(obs)
        action_numpy = action.cpu().numpy()[0]
        return action_numpy

    def sample(self, obs):
        obs = paddle.to_tensor(obs.reshape(1, -1), dtype='float32')
        action, _ = self.alg.sample(obs)
        action_numpy = action.cpu().numpy()[0]
        return action_numpy

    def learn(self, obs, action, reward, next_obs, terminal):
        terminal = np.expand_dims(terminal, -1)
        reward = np.expand_dims(reward, -1)

        obs = paddle.to_tensor(obs, dtype='float32')
        action = paddle.to_tensor(action, dtype='float32')
        reward = paddle.to_tensor(reward, dtype='float32')
        next_obs = paddle.to_tensor(next_obs, dtype='float32')
        terminal = paddle.to_tensor(terminal, dtype='float32')
        critic_loss, actor_loss = self.alg.learn(obs, action, reward, next_obs,
                                                 terminal)
        return critic_loss.cpu().numpy()[0], actor_loss.cpu().numpy()[0]
