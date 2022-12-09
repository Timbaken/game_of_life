from unittest import TestCase
from Simulator import *
from numpy.testing import assert_array_equal


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """

    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)
        state_one = np.array([[0, 0, 0, 0, 0],
                              [0, 0, 1, 1, 0],
                              [0, 0, 1, 1, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]])

        world1 = World(5)
        world1.world = state_one
        sim = Simulator(1, world1)
        self.assertIs(sim.get_world().world, state_one)
        sim.update()
        self.assertIs(sim.get_world().world, state_one)
        sim.update()
        self.assertIs(sim.get_world().world, state_one)
        sim.update()
        self.assertIs(sim.get_world().world, state_one)

        state_two = np.array([[0, 0, 0, 0, 0],
                              [0, 1, 1, 1, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]])
        state_three = np.array([[0, 0, 1, 0, 0],
                                [0, 1, 1, 0, 0],
                                [0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]])
        state_four = np.array([[0, 1, 1, 0, 0],
                               [0, 1, 1, 0, 0],
                               [0, 1, 1, 0, 0],
                               [0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0]])
        state_five = np.array([[0, 1, 1, 0, 0],
                               [1, 0, 0, 1, 0],
                               [0, 1, 1, 0, 0],
                               [0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0]])


        world2 = World(5)
        world2.world = state_two
        sim2 = Simulator(1, world2)
        self.assertIs(sim2.get_world().world, state_two)
        sim2.update()
        self.assertSequenceEqual(sim2.get_world().world.tolist(), state_three.tolist())
        sim2.update()
        self.assertSequenceEqual(sim2.get_world().world.tolist(), state_four.tolist())
        sim2.update()
        self.assertSequenceEqual(sim2.get_world().world.tolist(), state_five.tolist())
        sim2.update()
        self.assertSequenceEqual(sim2.get_world().world.tolist(), state_five.tolist())

        state_six = np.array([[0, 0, 1, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0]])
        state_seven = np.array([[0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 0],
                                [0, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]])
        state_eight = np.array([[0, 0, 1, 0, 0],
                                [0, 1, 0, 1, 0],
                                [0, 1, 0, 1, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0]])

        world3 = World(5)
        world3.world = state_six
        sim3 = Simulator(1, world3)
        self.assertIs(sim3.get_world().world, state_six)
        sim3.update()
        self.assertSequenceEqual(sim3.get_world().world.tolist(), state_seven.tolist())
        sim3.update()
        self.assertSequenceEqual(sim3.get_world().world.tolist(), state_eight.tolist())
        sim3.update()
        self.assertSequenceEqual(sim3.get_world().world.tolist(), state_eight.tolist())
        sim3.update()
        self.assertSequenceEqual(sim3.get_world().world.tolist(), state_eight.tolist())



        state_nine = np.array([[0, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [0, 1, 1, 1, 0],
                               [0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0]])
        state_ten = np.array([[0, 0, 0, 0, 0],
                              [0, 1, 1, 0, 0],
                              [0, 1, 1, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0]])
        state_eleven = np.array([[0, 0, 0, 0, 0],
                                 [0, 1, 1, 0, 0],
                                 [0, 0, 0, 1, 0],
                                 [0, 1, 1, 0, 0],
                                 [0, 0, 0, 0, 0]])
        state_twelve = np.array([[0, 0, 0, 0, 0],
                                 [0, 0, 1, 0, 0],
                                 [0, 0, 0, 1, 0],
                                 [0, 0, 1, 0, 0],
                                 [0, 0, 0, 0, 0]])
        state_thirteen = np.array([[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 1, 1, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0]])
        state_fourteen = np.array([[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0]])

        world4 = World(5)
        world4.world = state_nine
        sim4 = Simulator(1, world4)
        self.assertIs(sim4.get_world().world, state_nine)
        sim4.update()
        self.assertSequenceEqual(sim4.get_world().world.tolist(), state_ten.tolist())
        sim4.update()
        self.assertSequenceEqual(sim4.get_world().world.tolist(), state_eleven.tolist())
        sim4.update()
        self.assertSequenceEqual(sim4.get_world().world.tolist(), state_twelve.tolist())
        sim4.update()
        self.assertSequenceEqual(sim4.get_world().world.tolist(), state_thirteen.tolist())
        sim4.update()
        self.assertSequenceEqual(sim4.get_world().world.tolist(), state_fourteen.tolist())
        sim4.update()
        self.assertSequenceEqual(sim4.get_world().world.tolist(), state_fourteen.tolist())

        state_fifteen = np.array([[0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0],
                                  [0, 0, 6, 0, 0],
                                  [0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0]])
        state_sixteen = np.array([[0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0],
                                  [0, 0, 3, 0, 0],
                                  [0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0]])
        state_seventeen = np.array([[0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]])

        world5 = World(5)
        world5.world = state_fifteen
        sim5 = Simulator(6, world5)
        sim5.update()
        sim5.update()
        sim5.update()
        self.assertSequenceEqual(sim5.get_world().world.tolist(), state_sixteen.tolist())
        sim5.update()
        sim5.update()
        sim5.update()
        self.assertSequenceEqual(sim5.get_world().world.tolist(), state_seventeen.tolist())


    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)
