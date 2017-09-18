"""
LAB: (Un)informed Search
A01207563
"""

class State:

    def __init__(self, stacks_str):
        for ch in [' ', '(', ')']:
            stacks_str = stacks_str.replace(ch, '')
        stacks = stacks_str.split(';')
        self.stack_containers = []
        for stack in stacks:
            self.stack_containers.append([] if not stack else stack.split(','))     

    def __str__(self):
        state_str = ''
        for stack in self.stack_containers:
            state_str += ';(' + ','.join(stack) + ')'
        return state_str[1:]

    def result(self, action, height_limit):
        """Makes an action on the current state.
        PARAMS:
        - action: tuple 0: start, 1: finish representing movement of container.
        - height_limit: limit of the height of the stack.
        RETURNS:
        - True if the action was possible, False if not.
        """
        if len(self.stack_containers[action[1]]) < height_limit and self.stack_containers[action[0]]:
            container = self.stack_containers[action[0]].pop()
            self.stack_containers[action[1]].append(container)
            return True
        else:
            return False

    def possible_actions(self, visited_states, height_limit):
        """Generates the possible actions from a current state.
        PARAMS:
        - visited_states: set representing visited states.
        - height_limit: limit of the height of the stack.
        RETURNS:
        - List of tuples representing actions.
        """
        actions = []
        for i in range(len(self.stack_containers)):
            for j in range(i+1, len(self.stack_containers)):
                if self.result((i, j), height_limit):
                    if str(self) not in visited_states:
                        actions.append((i, j))
                    self.result((j, i), height_limit) # return to original state            
        for i in range(len(self.stack_containers)):
            for j in range(0, i):
                if self.result((i, j), height_limit):
                    if str(self) not in visited_states:
                        actions.append((i, j))
                    self.result((j, i), height_limit) # return to original state            
        return actions


state = State('(X, Y); (A, B); (C)')
print(state)
actions_l = state.possible_actions({}, 2)
print(actions_l)



