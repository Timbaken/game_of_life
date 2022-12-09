from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        change_list = []

        for x in range(self.world.width):
            for y in range(self.world.height):
                Neighbours = self.world.get_neighbours(x, y)
                alive_Neighbours = len([i for i, e in enumerate(Neighbours) if e != 0])
                if self.world.get(x, y) != 0 and alive_Neighbours < 2:
                    change_list.append((x, y, 0))
                elif self.world.get(x, y) != 0 and alive_Neighbours > 3:
                    change_list.append((x, y, 0))
                elif self.world.get(x, y) == 0 and alive_Neighbours == 3:
                    change_list.append((x, y, 1))

        for x, y, value in change_list:
            self.world.set(x, y, value)

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world