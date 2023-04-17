config = {
    "screen_width": 640,   #Szerokość ekranu
    "screen_height": 480,  #Wysokość ekranu
    "observation": {
        "type": "Kinematics",   #KinematicsObservation tworzy tablicę VxF, gdzie V to liczba pobliskich pojazdów,
                                # a F to zestaw odległości wymienionych w "features"
        "observation_shape": (10, 10),  #Pozwala na konwersję obrazu na skalę szarości
        "vehicles_count": 10,   #Liczba pojazdów najbliższych obserwowanemu pojazdowi
        "features": ["presence", "x", "y", "vx", "vy"], #Współrzędne pojazdów
        "features_range": {
            "x": [-100, 100],   #Globalne przesunięcie pojazdu obserwowanego lub przesunięcie względem pojazdu
                                # obserwowanego na osi x.
            "y": [-100, 100],   #Globalne przesunięcie pojazdu obserwowanego lub przesunięcie względem pojazdu
                                # obserwowanego na osi y.
            "vx": [-20, 20],    #Prędkość na osi x pojazdu.
            "vy": [-20, 20],    #Prędkość na osi y pojazdu.
        },
        "absolute": False, #Konfiguracja powoduje, że współrzędne "features" są wzgledem współrzędnych pojazdu głównego
        "order": "sorted",
    },
}