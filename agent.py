from rl.agents import DQNAgent, SARSAAgent, CEMAgent
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy

NB_STEPS = 10000  # Ilość kroków do wytrenowania modelu


def build_agent(model, actions):            #Funkcja tworząca Agenta
    policy = LinearAnnealedPolicy(          #Liniowa regresja  oblicza aktualną wartość progową i
                                            #przenosi ją do polityki wewnętrznej, która wybiera działanie.
                                            #Próg wartość podąża za funkcją liniową malejącą w czasie.
        EpsGreedyQPolicy(),                 #Polityka chciwa zwraca aktualnie najlepszą akcję zgodnie
                                            #z wartościami q_values
        attr="eps",
        value_max=1.0,
        value_min=0.1,
        value_test=0.2,
        nb_steps=NB_STEPS,
    )
    memory = SequentialMemory(limit=1000, window_length=3)      #Utworzenie pamięci Agenta
    dqn = DQNAgent(                         #Deep Q-Network
        model=model,                        #Przypisanie modelu dla Agenta
        memory=memory,                      #Przypisanie Agentowi pamięci
        policy=policy,                      #Polityka Agenta polegająca na podejmowaniu najbardziej obiecujących
                                            #działań
        enable_dueling_network=True,        #Mnożenie nagród przez podany czynnik
        dueling_type='avg',                 #Typ czynnika mnożenia nagród
        nb_actions=actions,                 #Akcje jakie są możliwe do wykonania przez Agenta
        nb_steps_warmup=NB_STEPS / 100,     #Liczba kroków zanim Agent rozpocznie naukę
    )
    CEMA = CEMAgent(                        #Cross Entropy Method (Metoda entropii krzyżowej)
        model = model,
        nb_actions = actions,
        memory = memory,
        batch_size=50,
        nb_steps_warmup=1000,
        train_interval=50,
        elite_frac=0.05,
        memory_interval=1,
        theta_init=None)
    SARSA = SARSAAgent(                     #SARSA Agent
        model=model,
        nb_actions=actions,
        policy=None,
        test_policy=None,
        gamma=0.99,
        nb_steps_warmup=10,
        train_interval=1)
    return dqn
