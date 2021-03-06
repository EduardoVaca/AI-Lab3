"""
LAB: (Un)informed Search
Algorithm: Uniform Cost-Search
A01207563
"""
import heapq
import problem_search_node
import problem_state
import utils


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
    heapq.heappush(frontier, problem_search_node.SearchNode(state, None, None, 0, 0))
    explored_set = set()
    while frontier:
        current_node = heapq.heappop(frontier)
        if utils.is_goal_state(current_node.state, goal_state):
            return utils.create_path_to_goal(current_node)
        explored_set.add(current_node.state.key())
        actions = current_node.state.possible_actions(explored_set, height_limit)
        for node in [current_node.child_node(action, height_limit) for action in actions]:
            heapq.heappush(frontier, node)
    return (-1, [])

def main():
    """Main method.
    """
    height_limit, state, goal_state = int(input()), problem_state.State(input()), utils.get_goal_state(input())    
    result = graph_search(state, goal_state, height_limit)
    if result[0] != -1:
        print(result[0])        
        print('; '.join([str(x) for x in result[1]]))
    else:
        print('No solution found')

if __name__ == '__main__':
    main()
