"""
LAB: (Un)informed Search
Algorithm: A* with consistent heuristic
A01207563
"""
import heapq
import problem_search_node
import problem_state

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

def get_heurisitc_cost_stacks(element, stack_index, goal_state, unused_stacks, unused_index):
    """Gets the heuristic cost of an element placed in a different stack
    PARAMS:
    - element : element to be moved
    - stack_index : current index of stack where the element is
    - goal_state : dictionary of goal state
    - unused_stacks : set of unused stacks
    - unused index : index of first unused stack
    RETURNS:
    - Cost of element in different stack
    """
    for k,v in goal_state.items():
        if element in v:
            return (abs(stack_index - k), v.index(element))
    if stack_index in unused_stacks:
        return (0, -1)
    else:
        return (abs(unused_index - stack_index), -1)

def get_heuristic_cost_height(element, height_index, height_dict):
    """Gets heuristic cost of an element in a different index height.
    PARAMS:
    - element : current element
    - height_index : index of current element
    - height_dict : dict of indexes with elements of goal state
    RETURNS:
    - Cost of element in different index stack
    """
    if element in height_dict:
        return abs(height_index - height_dict[element])
    else:
        return 0

def cons_heuristic(state, goal_state):
    """Method for calulating heuristic cost h(x)
    The heuristic is:
    1. Calculate de distance of an element to its goal stack
    2. Calculate difference of height index of that element with the goal position
    3. Do this for all elements
    4. Sum values
    PARAMS:
    - state : Current state of the problem
    - goal_state : Dict of goal state
    RETURNS:
    - Heuristic cost
    """ 
    unused_stacks = set(range(len(state.stack_containers))) - set(goal_state.keys())
    unused_index = list(unused_stacks)[0] if unused_stacks else -1
    cost = 0
    height_dict = {} # Dict for storing element and height index in goal state
    for i in range(len(state.stack_containers)):
        for element in state.stack_containers[i]:
            h_stack = get_heurisitc_cost_stacks(element, i, goal_state, unused_stacks, unused_index)
            cost += h_stack[0]            
            if h_stack[1] > -1:
                height_dict[element] = h_stack[1]                
    for i in range(len(state.stack_containers)):
        for j in range(len(state.stack_containers[i])):
            c = get_heuristic_cost_height(state.stack_containers[i][j], j, height_dict)
            cost += get_heuristic_cost_height(state.stack_containers[i][j], j, height_dict)            
    return cost

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
    """A* with consistent heuristic.
    PARAMS:
    - state : initial state
    - goal_state : dictionary of goal state
    - height_limit : limit of height of stacks
    RETURNS:
    - tuple of cost and path
    """
    frontier = []
    heapq.heappush(frontier, problem_search_node.SearchNode(state, None, None, 0))
    explored_set = set()
    while frontier:
        current_node = heapq.heappop(frontier)
        if is_goal_state(current_node.state, goal_state):
            return create_path_to_goal(current_node)
        explored_set.add(current_node.state.key())
        actions = current_node.state.possible_actions(explored_set, height_limit)
        for node in [current_node.child_node(action, height_limit, cons_heuristic, goal_state) for action in actions]:
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
