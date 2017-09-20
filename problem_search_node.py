import copy

class SearchNode:
    """Class that represents the node of the search.
    """

    def __init__(self, state, parent, action, path_cost, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.cost = cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def child_node(self, action_p, height_limit, heuristic = None, goal_state = None):
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
        cost = parent.cost + parent.state.step_cost(action)
        path_cost = cost + heuristic(state, goal_state) if heuristic and goal_state else cost
        return SearchNode(state, parent, action, path_cost, cost)