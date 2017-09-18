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
        if len(self.stack_containers[action[1]]) < height_limit and self.stack_containers[action[0]]:
            container = self.stack_containers[action[0]].pop()
            self.stack_containers[action[1]].append(container)
            return True
        else:
            return False


state = State('(X, Y,  Z); (); (C)')
print(state)
print(len(state.stack_containers[1]))
state.result((0, 1), 3)
print(state)
print(len(state.stack_containers[1]))
state.result((1, 2), 2)
print(state)
state.result((0, 2), 2)
print(state)



