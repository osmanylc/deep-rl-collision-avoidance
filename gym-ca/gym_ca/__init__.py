from gym.envs.registration import register

register(
    id='ca-v0',
    entry_point='gym_ca.envs:CAEnv'
)
