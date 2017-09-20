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
    cost = node.cost
    actions = []
    while node.action:
        actions.append(node.action)
        node = node.parent
    return (cost, actions[::-1])