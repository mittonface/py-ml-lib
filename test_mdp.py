from unittest import TestCase
from MDP import MDP
from MDP import State
from MDP import Action

class TestMDP(TestCase):
    """
    An MDP is essentially a non-deterministic weighted digraph.
    """
    def test_create_new_mdp(self):
        """
        I'm not sure what the create MDP method should actually do.
        """

        mdp = MDP()
        self.assertEqual(mdp.size(), 0)

        mdp = MDP(5)
        self.assertEqual(mdp.size(), 5)

        self.assertEqual(type(mdp.get_state(0)), State)
        self.assertEqual(mdp.get_state(4).id, 4)

        self.assertRaises(mdp.get_state(5), IndexError)

    def test_create_state(self):
        """
        For implementation simplification I'm imagining creating all of the the states separately and then
        connecting them afterwards by specifying the actions.
        """

        mdp = MDP()
        mdp.add_state(0)
        mdp.add_state(1)
        mdp.add_state(2)
        mdp.add_state(3)
        mdp.add_state(4)
        mdp.add_state(5, terminal=True)
        self.assertEqual(mdp.size(), 5)

        mdp = MDP()
        mdp.add_state("StateOne")
        mdp.add_state("StateTwo")
        mdp.add_state("StateThree")
        mdp.add_state("StateFour")
        self.assertEqual(mdp.size(), 4)

    def test_get_state(self):
        """
        Should probably be some nice way to get states by a state id or state name
        """
        mdp = MDP
        pass

    def test_mdp_size(self):
        """
        Probably nice to be able to tell the size of the MDP. If not only for tests
        """
        pass

    def test_add_action(self):
        """
        Every state should share a set of actions
        """
        pass

    def test_add_transition(self):
        """
        S, A, S', P
        Takes in a state, one of the actions, the state that we'll end up in after taking an action, and the probability
        that this transition occurs.
        """
        pass

    def test_validate(self):
        """
        Validate that the action probabilities add up to 1 for each state
        """
        pass