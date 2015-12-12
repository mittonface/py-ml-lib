from unittest import TestCase
from MDP import MDP
from MDP import State
from MDP import Action
import numpy as np

class TestAction(TestCase):

    def test_create_action(self):

        pass

    def test_create_named_action(self):
        pass

    def test_created_multiple_named_action_correct_ids(self):
        pass

class TestMDP(TestCase):
    """
    An MDP is essentially a non-deterministic weighted digraph.
    """
    def test_create_new_mdp_no_initial_states(self):
        """
        I'm not sure what the create MDP method should actually do.
        """

        # there isn't very much we can tell about an mdp that is completely devoid
        # of states
        mdp = MDP()
        self.assertEqual(mdp.num_states(), 0)

    def test_create_new_mdp_initial_num_states(self):
        """
        Test initializing MDPS with an explicity number of states
        """

        mdp = MDP(5)
        self.assertEqual(mdp.num_states(), 5)

        # this MDP should have 5 states
        self.assertEquals(type(mdp.get_state(0)), State)
        self.assertEquals(type(mdp.get_state(2)), State)
        self.assertEquals(type(mdp.get_state(4)), State)

    def test_create_new_mdp_init_num_states_populates_state_list(self):

        mdp = MDP(5)

        self.assertIn(mdp.get_state(0), mdp.get_state_list())
        self.assertIn(mdp.get_state(2), mdp.get_state_list())
        self.assertIn(mdp.get_state(4), mdp.get_state_list())

    def test_get_non_existing_state(self):
        """
        Test that you can't get a non existing state
        """
        mdp = MDP(5)

        with self.assertRaises(IndexError):
            mdp.get_state(5)

    def test_create_state(self):
        """
        For implementation simplification I'm imagining creating all of the the states separately and then
        connecting them afterwards by specifying the actions.
        """

        # States should be abled to be identified by numbers or by strings I suppose.
        # I don't imagine that strings will ever be used.
        mdp = MDP()
        mdp.add_state(0)
        mdp.add_state(1)
        mdp.add_state(2)
        mdp.add_state(3)
        mdp.add_state(4)
        mdp.add_state(5, terminal=True)
        self.assertEqual(mdp.num_states(), 6)

    def test_create_state_populates_state_list(self):
        mdp = MDP()

        mdp.add_state(0)
        mdp.add_state(2)

        self.assertIn(mdp.get_state(0), mdp.get_state_list())
        self.assertIn(mdp.get_state(2), mdp.get_state_list())

    def test_add_duplicate_state(self):
        mdp = MDP()

        mdp.add_state(0)
        with self.assertRaises(KeyError):
            mdp.add_state(0)

    def test_get_state(self):
        """
        Should probably be some nice way to get states by a state id or state name
        """

        # test that you can get a state by numerical id
        mdp = MDP()
        mdp.add_state(0)
        self.assertEquals(type(mdp.get_state(0)), State)
        self.assertIn(mdp.get_state(0), mdp.get_state_list())

    def test_get_non_existent_state(self):
        mdp = MDP(5)

        with self.assertRaises(IndexError):
            self.assertRaises(mdp.get_state(11), IndexError)

    def test_mdp_size(self):
        """
        Probably nice to be able to tell the size of the MDP. If not only for tests
        """
        mdp = MDP()
        self.assertEqual(mdp.num_states(), 0)

        mdp = MDP(5)
        self.assertEqual(mdp.num_states(), 5)

        mdp = MDP()
        mdp.add_state(0)
        mdp.add_state(1)
        self.assertEqual(mdp.num_states(), 2)


    def test_add_action(self):
        """
        Test that you can add an action. Named actions make more sense than named states
        """
        mdp = MDP()

        mdp.add_action(0)
        self.assertEqual(mdp.num_actions(), 1)
        self.assertEqual(type(mdp.get_action(0)), Action)
        self.assertIn(mdp.get_action(0), mdp.get_action_list())

    def test_add_string_action(self):
        mdp = MDP()
        mdp.add_action("jump")
        self.assertEqual(mdp.num_actions(), 1)
        self.assertEqual(type(mdp.get_action("jump")), Action)
        self.assertIn(mdp.get_action("jump"), mdp.get_action_list())


    def test_add_duplicate_action(self):
        mdp = MDP()
        mdp.add_action("jump")
        with self.assertRaises(KeyError):   # RunTime error is probably more appropriate?
            mdp.add_action("jump")


    def test_get_num_actions(self):
        """
        It will be helpful to be able to return the number of distinct actions that an MDP
        has.
        """
        mdp = MDP()
        mdp.add_action(0)
        mdp.add_action(1)
        mdp.add_action(2)
        mdp.add_action(3)
        mdp.add_action(4)
        mdp.add_action(5)
        mdp.add_action(6)

        action_list = mdp.get_action_list()
        self.assertEqual(len(action_list), 7)
        self.assertIn(mdp.get_action(0), action_list)


    def test_get_action_list(self):
        mdp = MDP()

        mdp.add_action(0)
        mdp.add_action(1)

        action_list = mdp.get_action_list()
        self.assertEqual(len(action_list), 2)
        self.assertIn(mdp.get_action(0), action_list)

    def test_add_transition(self):
        """
        S, A, S', P
        Takes in a state, one of the actions, the state that we'll end up in after taking an action, and the probability
        that this transition occurs.
        """

        mdp = MDP(5)
        mdp.add_action(0)

        s = mdp.get_state(0)
        a = mdp.get_action(0)
        s_prime = mdp.get_state(1)

        mdp.add_transition(s, a, s_prime, 1.)

        transition_function = mdp.get_transition_function()
        self.assertEqual(s.id, a.id)


    def test_get_transition_probability(self):
        pass



    def test_validate(self):
        """
        Validate that the action probabilities add up to 1 for each state
        """
        pass


    def test_get_state_list(self):
        """
        It might be helpful to be able to get a list of all the states
        """

        mdp = MDP(5)
        state_list = mdp.get_state_list()

        self.assertEqual(len(state_list), 5)
        self.assertIn(mdp.get_state(0), state_list)