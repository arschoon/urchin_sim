from distutils.log import info
import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
from gym.envs.registration import register


class URCHINEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(
        self,
        xml_file = "/home/geoffrey/Research/git/urchin_sim/urchin.xml",
    ):
        utils.EzPickle.__init__(**locals())
        register(id = 'URCHIN-v0', entry_point= "URCHIN_SIM.urchin:URCHINEnv")
        mujoco_env.MujocoEnv.__init__(self, xml_file, 5)


    def step(self, action):
        self.do_simulation(action, self.frame_skip)
        done = False

        observation = np.array([])
        reward = 0
        info = {}

        return observation, reward, done, info
    
    def reset_model(self):
        observation = np.array([])
        return observation
