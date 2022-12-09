from Visualisation import *
from Simulator import *
import time

grid_width = 10
grid_heigth = 10

# Configuratie
VISUALISATION=True
# VISUALISATION=False

if __name__ == "__main__":


    w = World(grid_width, grid_heigth)
    sim = Simulator(w)

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)