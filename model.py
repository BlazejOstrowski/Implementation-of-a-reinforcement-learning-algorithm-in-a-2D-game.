
from keras.models import Sequential
from keras.layers import Dense, Flatten, Convolution2D


def build_model(height, width, actions):  #Stworzenie funkcji uczącej sieć i zwracającej wyuczony model
    model = Sequential()  #Stworzenie modelu sekwencyjnego
    model.add(
        Convolution2D(    #Tworzenie warstw konwolucyjnych
            64,
            (4, 4),
            strides=(2, 2),
            activation="relu",
            input_shape=(3, height, width),
            padding="same",
        )  #Stworzenie warstwy konwolucyjnej
    )
    model.add(Convolution2D(32, (2, 2), strides=(1, 1), activation="relu", padding="same"))
    model.add(Convolution2D(32, (2, 2), activation="relu", padding="same"))
    model.add(Flatten())                            #Utworzenie warstwy spłaszczającej
    model.add(Dense(512, activation="relu"))        #Utworzenie warstw Dense
    model.add(Dense(256, activation="relu"))
    model.add(Dense(actions, activation="linear"))
    return model

