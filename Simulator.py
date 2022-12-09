from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, birthage = 1, world = None, default_birth_and_survival = True, submissive_and_breedable = [1,2,3,4,5,6,7,8,9]):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

        if default_birth_and_survival:
            self.birth = [3]
            self.survival = [2, 3]
        else:
            self.birth, self.survival = self.birth_and_survival_input()

        self.birthage = birthage
        self.submissive_and_breedable = submissive_and_breedable


    def birth_and_survival_input(self):
        while True:
            try:
                birth = int(input('bij hoeveel worden ze geboren?'))
                for i in str(birth):
                    if i == '9':
                        raise ValueError
                else:
                    break
            except ValueError:
                print('invalide input')
                continue
        while True:
            try:
                survival = int(input('bij hoeveel blijven ze leven?'))
                for i in str(survival):
                    if i == '9':
                        raise ValueError
                else:
                    break
            except ValueError:
                print('invalide input')
                continue
        return [int(x) for x in str(birth)], [int(x) for x in str(survival)]
    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        change_list = []

        #TODO: Do something to evolve the generation
        for x in range(self.world.width):
            for y in range(self.world.height):
                Neighbours = self.world.get_neighbours(x, y)
                alive_Neighbours = len([i for i, e in enumerate(Neighbours) if e != 0])
                submissive_and_breedable = len([i for i in Neighbours if i in self.submissive_and_breedable])
                if self.world.get(x, y) != 0 and alive_Neighbours not in self.survival:
                    change_list.append((x, y, self.world.get(x, y) - 1))
                elif self.world.world[y][x] == 0 and submissive_and_breedable in self.birth:
                    change_list.append((x, y, self.birthage))

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