import ucs
import run
import problem_state
import utils
import a_star_incons


def print_result(result):
    if result[0] != -1:
        print(result[0])        
        print('; '.join([str(x) for x in result[1]]))
    else:
        print('No solution found')

def do_search(states, goals):
    for i in range(len(states)):
        print_result(ucs.graph_search(problem_state.State(states[i]), utils.get_goal_state(goals[i]), 5))
        print_result(run.graph_search(problem_state.State(states[i]), utils.get_goal_state(goals[i]), 5))
        print_result(a_star_incons.graph_search(problem_state.State(states[i]), utils.get_goal_state(goals[i]), 5))
        print('-------------------')


my_states = [
    '(A);(B);(C)',
    '(A);(B);(C)',
    '(A);(B);(C)',
    '(B, A); (C, D, E); ()',
    '(X, Y, Z); (); ()',
    '(X, Y, Z); (); (A, B, C)',
    '(A, B); (C, D); (); ()',
    '(A, B, C); (D, E, F); (); ()',
    '(A, B, C); (D, E, F); ()',
]
my_goals = [
    '(A,C);X;X',
    '(A,C);X;(B)',
    '(C, A);X;(B)',
    '(A, E); (B); (D, C)',
    '(); (X, Y, Z); ();',
    '(A, B, C); (X, Y, Z); ();',
    '(A, C); (B, D); (); ()',
    '(A, C, E); (B, D, F); (); ()',
    '(A, C, E, F); X; X;',
]

do_search(my_states, my_goals)