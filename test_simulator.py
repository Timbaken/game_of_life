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
        sim1 = Simulator(world1)
        self.assertSequenceEqual(sim1.get_world().world.tolist(), state_one.tolist())
        sim1.update()
        self.assertSequenceEqual(sim1.get_world().world.tolist(), state_one.tolist())
        sim1.update()
        self.assertSequenceEqual(sim1.get_world().world.tolist(), state_one.tolist())
        sim1.update()
        self.assertSequenceEqual(sim1.get_world().world.tolist(), state_one.tolist())

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
        sim2 = Simulator(world2)
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
        sim3 = Simulator(world3)
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
                               [0, 1, 1, 1, 0],
                               [0, 1, 1, 1, 1],
                               [0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0]])
        state_ten = np.array([[0, 0, 1, 0, 0],
                               [1, 0, 0, 0, 1],
                               [1, 0, 0, 0, 1],
                               [0, 0, 1, 1, 0],
                               [0, 0, 0, 0, 0]])
        state_eleven = np.array([[0, 0, 0, 0, 0],
                               [0, 1, 0, 1, 0],
                               [0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 1],
                               [0, 0, 1, 1, 0]])
        state_twelve = np.array([[0, 0, 0, 1, 0],
                               [0, 0, 1, 0, 0],
                               [1, 0, 0, 1, 1],
                               [0, 0, 0, 0, 1],
                               [0, 0, 1, 0, 1]])
        state_thirteen = np.array([[0, 0, 1, 0, 0],
                               [0, 0, 1, 0, 0],
                               [1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1]])
        state_fourteen = np.array([[0, 0, 0, 1, 0],
                               [0, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0]])
        state_fiveteen = np.array([[0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]])

        world4 = World(5)
        world4.world = state_nine
        sim4 = Simulator(world4, [3], [2])
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
        self.assertSequenceEqual(sim4.get_world().world.tolist(), state_fiveteen.tolist())
        sim4.update()
        self.assertSequenceEqual(sim4.get_world().world.tolist(), state_fiveteen.tolist())

        state_sixteen = np.array([[0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0],
                                  [0, 0, 6, 0, 0],
                                  [0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0]])
        state_seventeen = np.array([[0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0],
                                  [0, 0, 3, 0, 0],
                                  [0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0]])
        state_eighteen = np.array([[0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]])
        world5 = World(5)
        world5.world = state_sixteen
        sim5 = Simulator(world5, [3], [2, 3], 6)
        sim5.update()
        sim5.update()
        sim5.update()
        self.assertSequenceEqual(sim5.get_world().world.tolist(), state_seventeen.tolist())
        sim5.update()
        sim5.update()
        sim5.update()
        self.assertSequenceEqual(sim5.get_world().world.tolist(), state_eighteen.tolist())

        state_nineteen = np.array([[0, 0, 0, 0, 0],
                                   [0, 6, 0, 6, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 6, 0, 0],
                                   [0, 0, 0, 0, 0]])
        state_twenty = np.array([[0, 0, 0, 0, 0],
                                   [0, 5, 0, 5, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 5, 0, 0],
                                   [0, 0, 0, 0, 0]])
        state_twentyone = np.array([[0, 0, 0, 0, 0],
                                 [0, 4, 0, 4, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 4, 0, 0],
                                 [0, 0, 0, 0, 0]])
        state_twentytwo = np.array([[0, 0, 0, 0, 0],
                                    [0, 3, 0, 3, 0],
                                    [0, 0, 6, 0, 0],
                                    [0, 0, 3, 0, 0],
                                    [0, 0, 0, 0, 0]])

        world6 = World(5)
        world6.world = state_nineteen
        sim6 = Simulator(world6, birthage=6, submissive_and_breedable=[2,3,4])
        self.assertSequenceEqual(sim6.get_world().world.tolist(), state_nineteen.tolist())
        sim6.update()
        self.assertSequenceEqual(sim6.get_world().world.tolist(), state_twenty.tolist())
        sim6.update()
        self.assertSequenceEqual(sim6.get_world().world.tolist(), state_twentyone.tolist())
        sim6.update()
        self.assertSequenceEqual(sim6.get_world().world.tolist(), state_twentytwo.tolist())


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
