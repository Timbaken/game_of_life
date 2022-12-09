from unittest import TestCase
from World import *


class TestWorld(TestCase):
    """
    Test cases for ``World`` data type.
    """
    def setUp(self):
        """
        Common setup for running tests
        """
        self.width, self.height = 10, 12
        self.world = World(self.width, self.height)

    def test_set(self):
        """
        Tests setting value on location (x,y).
        """
        x, y = 4, 6
        self.world.set(x, y)
        self.assertEqual(self.world.world[y][x], 1)
        value = 7
        self.world.set(x, y, 7)
        self.assertEqual(self.world.world[y][x], 7)

    def test_get(self):
        """
        Tests getting value from location (x, y).
        """
        x, y = 3, 5
        value = 3
        self.world.world[y][x] = 3
        self.assertEqual(self.world.get(x, y), value)

    def test_get_neighbours(self):
        """
        Tests getting neighbours from location.
        """
        x, y = 2, 0
        value = 4
        self.world.set(x, self.height-1, value)
        # print(self.world.world)
        neighbours = self.world.get_neighbours(x, y)
        # print(neighbours)
        self.assertEqual(8, len(neighbours))
        self.assertIn(value, neighbours)

    def test_get_agents(self):
        """
        Tests getting all the agents in the world
        """

        self.world.set(0, 0)
        self.world.set(1, 1)
        self.world.set(3, 4)

        agents = self.world.get_agents()

        self.assertEqual([(0, 0), (1, 1), (3, 4)], agents)


        # self.assertEqual(self.world.get(x, y), value)
        # self.assertEqual(self.world.get(x, y), value)
        # self.assertEqual(self.world.get(x, y), value)
