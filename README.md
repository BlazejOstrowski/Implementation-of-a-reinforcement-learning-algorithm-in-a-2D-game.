# Implementation-of-a-reinforcement-learning-algorithm-in-a-2D-game.

The goal of this project is to implement a reinforcement learning algorithm in a 2D game available on the gymlibrary.dev website (previously gym.openai). It involves controlling a simple, rectangular vehicle on a multi-lane road. Our task is to avoid other cars, while highly-scored actions include staying in the right lane for as long as possible and maintaining the highest possible speed. In the repository, this type of gameplay is called "highway-v0" from a collection of various scenarios called "highway-env".

The two strategies a player can follow are slow but safe driving for an extended period or fast movement, which carries a higher risk of collision with another road user. Assuming that the time to collect the most points is limited, the user must decide which approach is most suitable for them.

The simulation environments prepared by developers are adapted to provide all the necessary information to solve such problems. Therefore, capturing the image and extracting features based on it is not necessary. There is also extensive documentation describing various functions needed to obtain data from sensors placed on the car we control.

A very useful aspect of this environment is also the ability to run the program without rendering the screen. This means that the final learning process, after the process of removing shortcomings and errors in the code, will run much faster. This should allow for even better results of our simulations due to the saved time, which can be devoted to better adjusting the variables in the model.

The final stage of this project will be comparing the results of our model with our personal attempts. Then we will try to determine what causes the most significant problems for the program and what causes them.
