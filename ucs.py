"""
LAB: (Un)informed Search
A01207563
"""

class State:

    def __init__(self, stacks_str):
        for ch in [' ', '(', ')']:
            stacks_str = stacks_str.replace(ch, '')
        stacks = stacks_str.split(';')
        self.container_stacks = []
        for stack in stacks:
            self.container_stacks.append(stack.split(','))     

    def __str__(self):
        state_str = ''
        for stack in self.container_stacks:
            state_str += ';(' + ','.join(stack) + ')'
        return state_str[1:]

state = State('(x, y,  z); (); (C)')
print(state)


