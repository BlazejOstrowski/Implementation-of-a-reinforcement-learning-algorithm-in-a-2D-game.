# Implementation-of-a-reinforcement-learning-algorithm-in-a-2D-game.

The goal of this project is to implement a reinforcement learning algorithm in a 2D game available on the gymlibrary.dev website (previously gym.openai). It involves controlling a simple, rectangular vehicle on a multi-lane road. Our task is to avoid other cars, while highly-scored actions include staying in the right lane for as long as possible and maintaining the highest possible speed. In the repository, this type of gameplay is called "highway-v0" from a collection of various scenarios called "highway-env".

The two strategies a player can follow are slow but safe driving for an extended period or fast movement, which carries a higher risk of collision with another road user. Assuming that the time to collect the most points is limited, the user must decide which approach is most suitable for them.

The simulation environments prepared by developers are adapted to provide all the necessary information to solve such problems. Therefore, capturing the image and extracting features based on it is not necessary. There is also extensive documentation describing various functions needed to obtain data from sensors placed on the car we control.

A very useful aspect of this environment is also the ability to run the program without rendering the screen. This means that the final learning process, after the process of removing shortcomings and errors in the code, will run much faster. This should allow for even better results of our simulations due to the saved time, which can be devoted to better adjusting the variables in the model.

The final stage of this project will be comparing the results of our model with our personal attempts. Then we will try to determine what causes the most significant problems for the program and what causes them.

# Results
Based on the results of our observations, we can conclude that the created model is learning, which is confirmed by the rewards we receive with increasing iterations depicted in Fig. Each point on the chart represents an average of the previous 1000 measurements.

![image](https://user-images.githubusercontent.com/104165382/232477088-87f59af5-4ca6-461a-a89d-25f30b5e6d2d.png)

In Fig., we can observe that the actual increase in rewards for learning is noticeable from approximately 300,000 iterations. Further learning would likely yield better results, but we could not prove this empirically using the approach we adopted in our project. However, we can see that after 600,000 iterations, the increase in rewards becomes significant, and despite the fact that fluctuations will likely still occur, we can conclude that for about 1,000,000 iterations, the increase in reward values would be clearly visible. The results we obtained allow us to determine that the trend of receiving increasingly larger rewards is undoubtedly increasing.

The implementation of the environment itself significantly limited our research due to the long learning time. It was possible to accelerate the evaluation of the algorithm using CuLE, which is a CUDA port. It is used to evaluate deep reinforcement learning algorithms in Atari games. CuLE scales to systems with multiple GPUs and renders directly on the GPU, avoiding bottlenecks resulting from limited CPU-GPU communication bandwidth. Unfortunately, after analyzing, we concluded that the implementation of CuLE, which requires the use of the PyTorch library, is relatively complicated compared to the final results, and we ultimately abandoned the idea.

Based on the operation of the program and the results obtained, we can conclude that with the adopted configuration of the algorithm, the model using convolutional neural networks for learning, and the DQNAgent responsible for awarding rewards, our algorithm fundamentally works well. A possible change of the agent to CEMA or SARSA does not seem to result in better algorithm performance, which we infer from a review of the literature on other agent algorithms.

Further attempts to change the policy based on which rewards are assigned in the agent could be possible. However, in our project, the use of linear regression seems to be an optimal solution.
