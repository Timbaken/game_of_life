from World import *


class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world=None, birth=None, survival=None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world is None:
            self.world = World(20)
        else:
            self.world = world

        if birth is None:
            self.birth = [3]
        else:
            self.birth = birth

        if survival is None:
            self.survival = [2, 3]
        else:
            self.survival = survival

    # def birth_and_survival_input(self, birth_or_survival):
    #     while True:
    #         try:
    #             birth_survival = int(input(f"bij hoeveel {'worden ze geboren?' if birth_or_survival == 'birth' else 'blijven ze leven?'}?"))
    #             for i in str(birth_survival):
    #                 if i == '9':
    #                     raise ValueError
    #             else:
    #                 break
    #         except ValueError:
    #             print('invalide input')
    #             continue
    #
    #     return [int(x) for x in str(birth_survival)]

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
                if self.world.get(x, y) != 0 and alive_Neighbours not in self.survival:
                    change_list.append((x, y, 0))
                elif self.world.get(x, y) == 0 and alive_Neighbours in self.birth:
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
