class MDP(object):
    """
    An MDP is basically just a finite state machine, with the exception being that the actions you can
    take in each state don't need to deterministically take you to the next state. The other main difference
    is that you generally get some reward for entering a state, or taking an action and entering a state, or
    being in a state, taking an action, and ending up in a state.

    More Formally:

    An MDP is defined as a tuple (S, A, R, T)

    S: Is a set of States.
    A: Is a set of actions
    R: is a reward function of the form
        R(s') -> r
           where s' is a state from S, r is a real number
           - you get the reward based on the state you enter

        R(a, s') -> r
           where a is an action from A.
           - you get the reward based on the action you've taken and the state you entered.

        R(s, a, s') -> r
           where s, s' are states from S
           - you get the reward based on the state you're leaving, the action you take and the state you enter.
             this is the most general form. But not necessarily always needed.

    T : is a transition function of the form
        T(s, a, s') -> p
        s, s' are states from S
        a is an action from A
        p is the probability of the transition occurring

        e.g. T(0, 1, 1) - should return the probability of ending up in state 1. Given that you started in state 0
                          and took action 1.

        Notes:
            The probability function should return a proper probability distribution across all state action pairs.

            e.g. If you have 3 actions: a1, a2, a3.
                T(0, a1, s') -> p1
                T(0, a2, s') -> p2
                T(0, a3, s') -> p3

            p1 + p2 + p3 == 1.
    """

    def __init__(self, num_states = 0):
        self.states = {}
        self.actions = []
        self.transitions = []

        if num_states > 0:
            for id in range(num_states):
                self.add_state(id)

    def add_state(self, id, terminal=False):
        try:
            self.get_state(id)
            raise KeyError
        except IndexError:
            self.states[id] = State(id, terminal)

    def get_state(self, id):
        if id in self.states:
            return self.states[id]
        raise IndexError

    def add_action(self, id):
        action = self.get_action(id)
        if action is None:
            self.actions.append(Action(id))
        else:
            raise KeyError

    def get_action(self, id):
        for action in self.actions:
            if action.id is id:
                return action
        return None

    def add_transition(self, state, action, new_state, probability=1.):
        pass

    def validate(self):
        pass

    def num_states(self):
        return len(self.states)

    def num_actions(self):
        return len(self.actions)

    def get_action_list(self):
        return self.actions

    def get_state_list(self):
        return list(self.states.values())

    def get_transition_function(self):
        return self.transitions

class State(object):
    """
    A state really doesn't have too much functionality. But it could be the case that we want to extend it
    to have some sort of functionality at some point.

    They're really just something that you reference right now.
    """
    def __init__(self, id, terminal=False):
        self.id = id
        self.terminal = False


class Action(object):
    """
    An action is like a state in that it doesn't have too much functionality.
    """
    def __init__(self, id):
        self.id = id
