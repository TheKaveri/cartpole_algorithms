from gymnasium.envs.registration import register

register(
    id="ContinuousCartPole-v0",
    entry_point="custom_envs.continuous_cartpole:ContinuousCartPoleEnv",
)
