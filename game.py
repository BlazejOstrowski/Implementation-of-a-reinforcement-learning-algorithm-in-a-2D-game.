import gym
import highway_env
from agent import build_agent, NB_STEPS
from conf import config
from model import build_model
from keras.optimizers import Adam
import matplotlib.pyplot as plt
import os
# from ray.rllib.algorithms.ppo import PPOConfig
import random

HOW_MANY_EPISODES = 10  #Ilość epizodów do celów testowych
# ACTIONS_ALL = {0: "Lewo", 1: "Bezczynny", 2: "Prawo", 3: "Szybciej", 4: "Wolniej"}


def plot_results(data):
    plt.plot(
        data.history["nb_steps"],
        data.history["episode_reward"],
    )
    plt.ylabel("Reward")
    plt.xlabel("Iteration")
    plt.show()


env = gym.make("highway-fast-v0")
# PPOConfig()
env.configure(config)
actions = env.get_available_actions()
# print(actions)
env.reset()
height, width = env.observation_space.shape

# episodes = 3
# for episode in range(1, episodes):
#     state = env.reset()
#     done = False

#     while not done:
#         env.render()
#         # print(f"{n_state=}")
# env.close()

model = build_model(height, width, len(actions))
dqn = build_agent(model, len(actions))

load = input("Do You want to load a already trained model?(y/n): ").lower()
if len(os.listdir("saved_weights/")) == 0 and load == "y":
    print("Directory with models is empty. Exiting.")
    exit()
elif load == "y":
    dqn.load_weights("saved_weights/1k-fast.h5f")
    scores = dqn.test(env, nb_episodes=HOW_MANY_EPISODES, visualize=True)
    plot_results(scores)
else:
    dqn.compile(Adam(lr=1e-4))
    training = dqn.fit(env, nb_steps=NB_STEPS, visualize=False, verbose=2)
    scores = dqn.test(env, nb_episodes=HOW_MANY_EPISODES, visualize=True)
    plot_results(training)
    dqn.save_weights("saved_weights/1k-fast.h5f")
# print(np.mean(scores.history["episode_reward"]))
