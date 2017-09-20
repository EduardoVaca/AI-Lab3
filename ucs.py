"""
LAB: (Un)informed Search
A01207563
"""
import copy
import heapq
import problem_state

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

    def child_node(self, action_p, height_limit):
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
        path_cost = parent.path_cost + parent.state.step_cost(action)
        return SearchNode(state, parent, action, path_cost)

def get_goal_state(state_str):
    """Creates a dict with indexes and meaningful stack_container goal values.
    PARAMS:
    - state_str : state string
    RETURNS:
    - dictionary of goal state
    """
    for ch in [' ', '(', ')']:
        state_str = state_str.replace(ch, '')
    stacks = state_str.split(';')
    return {i: stacks[i].split(',') for i in range(len(stacks)) if stacks[i] and stacks[i] != 'X'}

def is_goal_state(state, goal_state):
    """Checks if a state is goal state
    PARAMS:
    - state : current state
    - goal_state : dictionary of goal state
    RETURNS:
    - true if goal state, else false
    """
    for k,v in goal_state.items():
        if state.stack_containers[k] != v:
            return False
    return True

def create_path_to_goal(node):
    """Create the path from goal node to initial node.
    PARAMS:
    - node : goal node
    RETURNS:
    - tuple with cost and list of actions
    """
    cost = node.path_cost
    actions = []
    while node.action:
        actions.append(node.action)
        node = node.parent
    return (cost, actions[::-1])

def graph_search(state, goal_state, height_limit):
    """Uniform Cost-Search.
    PARAMS:
    - state : initial state
    - goal_state : dictionary of goal state
    - height_limit : limit of height of stacks
    RETURNS:
    - tuple of cost and path
    """
    frontier = []
    heapq.heappush(frontier, SearchNode(state, None, None, 0))
    explored_set = set()
    while frontier:
        current_node = heapq.heappop(frontier)
        if is_goal_state(current_node.state, goal_state):
            return create_path_to_goal(current_node)
        explored_set.add(current_node.state.key())
        actions = current_node.state.possible_actions(explored_set, height_limit)
        for node in [current_node.child_node(action, height_limit) for action in actions]:
            heapq.heappush(frontier, node)
    return (-1, [])

def main():
    """Main method.
    """
    height_limit, state, goal_state = int(input()), problem_state.State(input()), get_goal_state(input())    
    result = graph_search(state, goal_state, height_limit)
    if result[0] != -1:
        print(result[0])        
        print('; '.join([str(x) for x in result[1]]))
    else:
        print('No solution found')

if __name__ == '__main__':
    main()
