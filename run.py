"""
LAB: (Un)informed Search
Algorithm: A* with consistent heuristic
A01207563
"""
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
    for k,v in goal_state.items():
        if element in v:
            return (abs(stack_index - k), v.index(element))
    if stack_index in unused_stacks:
        return (0, -1)
    else:
        return (abs(unused_index - stack_index), -1)

def get_heuristic_cost_height(element, height_index, height_dict):
    if element in height_dict:
        return abs(height_index - height_dict[element])
    else:
        return 0

def cons_heuristic(state, goal_state):    
    unused_stacks = set(range(len(state.stack_containers))) - set(goal_state.keys())
    print(set(goal_state.keys()))
    print(set(range(len(state.stack_containers))))
    print(unused_stacks)
    unused_index = list(unused_stacks)[0] if unused_stacks else -1
    cost = 0
    height_dict = {} # Dict for storing element and height index in goal state
    for i in range(len(state.stack_containers)):
        for element in state.stack_containers[i]:
            h_stack = get_heurisitc_cost_stacks(element, i, goal_state, unused_stacks, unused_index)
            cost += h_stack[0]
            print('adding {} for e {} in stack'.format(h_stack[0], element))
            if h_stack[1] > -1:
                height_dict[element] = h_stack[1]
                print('element {} has height {} on goal'.format(element, h_stack[1]))
    for i in range(len(state.stack_containers)):
        for j in range(len(state.stack_containers[i])):
            c = get_heuristic_cost_height(state.stack_containers[i][j], j, height_dict)
            cost += get_heuristic_cost_height(state.stack_containers[i][j], j, height_dict)
            print('adding {} for e {} in height'.format(c, state.stack_containers[i][j]))
    return cost

def main():
    """Main method.
    """
    height_limit, state, goal_state = int(input()), problem_state.State(input()), get_goal_state(input())    
    print(cons_heuristic(state, goal_state))

if __name__ == '__main__':
    main()
