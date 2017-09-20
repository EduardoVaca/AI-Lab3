import copy

class SearchNode:
    """Class that represents the node of the search.
    """

    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def child_node(self, action_p, height_limit, heuristic = None):
        """Method that creates a child node of node.
        PARAMS:
        - action_p : action to be applied.
        RETURNS:
        - new search node.
        """
        state = copy.deepcopy(self.state)
        state.result(action_p, height_limit)
        parent = self
        action = action_p
        if heuristic:
            path_cost = parent.path_cost + parent.state.step_cost(action) + heuristic(state)
        else:
            path_cost = parent.path_cost + parent.state.step_cost(action)
        return SearchNode(state, parent, action, path_cost)