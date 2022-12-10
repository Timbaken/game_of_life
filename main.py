from Visualisation import *
from Simulator import *
import time

grid_width = 5
grid_heigth = 5

# Configuratie
VISUALISATION=True
# VISUALISATION=False

if __name__ == "__main__":


    w = World(grid_width, grid_heigth)
    sim = Simulator(w, [3], [2, 3])

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)