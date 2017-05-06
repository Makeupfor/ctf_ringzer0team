from requests import get
from copy import deepcopy
from pexpect import pxssh
import re
from time import sleep

N = 9

def output(a):
    print(a)

def print_field(field):
    answer = ''
    if not field:
        output("No solution")
        return
    for i in range(N):
        for j in range(N):
            cell = field[i][j]
            if cell == 0 or isinstance(cell, set):
                output('.')
            else:                
                answer = answer + str(cell)           
    return answer

def read(field):
    """ Read field into state (replace 0 with set of possible values) """

    state = deepcopy(field)
    for i in range(N):
        for j in range(N):
            cell = state[i][j]
            if cell == 0:
                state[i][j] = set(range(1,10))

    return state

def done(state):
    """ Are we done? """

    for row in state:
        for cell in row:
            if isinstance(cell, set):
                return False
    return True


def propagate_step(state):
    """ Propagate one step """

    new_units = False

    for i in range(N):
        row = state[i]
        values = set([x for x in row if not isinstance(x, set)])
        for j in range(N):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    state[i][j] = state[i][j].pop()
                    new_units = True
                elif len(state[i][j]) == 0:
                    return False, None

    for j in range(N):
        column = [state[x][j] for x in range(N)]
        values = set([x for x in column if not isinstance(x, set)])
        for i in range(N):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    state[i][j] = state[i][j].pop()
                    new_units = True
                elif len(state[i][j]) == 0:
                    return False, None

    for x in range(3):
        for y in range(3):
            values = set()
            for i in range(3*x, 3*x+3):
                for j in range(3*y, 3*y+3):
                    cell = state[i][j]
                    if not isinstance(cell, set):
                        values.add(cell)
            for i in range(3*x, 3*x+3):
                for j in range(3*y, 3*y+3):
                    if isinstance(state[i][j], set):
                        state[i][j] -= values
                        if len(state[i][j]) == 1:
                            state[i][j] = state[i][j].pop()
                            new_units = True
                        elif len(state[i][j]) == 0:
                            return False, None

    return True, new_units

def propagate(state):
    """ Propagate until we reach a fixpoint """

    while True:
        solvable, new_unit = propagate_step(state)
        if not solvable:
            return False
        if not new_unit:
            return True


def solve(state):
    """ Solve sudoku """

    solvable = propagate(state)

    if not solvable:
        return None

    if done(state):
        return state

    for i in range(N):
        for j in range(N):
            cell = state[i][j]
            if isinstance(cell, set):
                for value in cell:
                    new_state = deepcopy(state)
                    new_state[i][j] = value
                    solved = solve(new_state)
                    if solved is not None:
                        return solved
                return None

def main():
    field = []
    solution = 'invalid'

    s = pxssh.pxssh()
    s.login('ringzer0team.com', port=12643, username='sudoku', password='dg43zz6R0E', terminal_type='vt100', original_prompt='Solution:', auto_prompt_reset=False)
    s.PROMPT='Solution:'    
    ret = s.before.splitlines()

    for line in ret:
        match_line = re.search('\| ([\d\s]) \| ([\d\s]) \| ([\d\s]) \| ([\d\s]) \| ([\d\s]) \| ([\d\s]) \| ([\d\s]) \| ([\d\s]) \| ([\d\s]) \|', line)
        if match_line:
            field_line = [] 
            for i in range(1,10):                
                if match_line.group(i) == ' ':
                    field_line.append(0)
                else:
                    field_line.append(int(match_line.group(i)))
            field.append(field_line)  

    state = read(field)
    tmp = print_field(solve(state))
    print tmp
    
    answer = ''
    for i in tmp:
        answer = answer + i + ','
    answer = answer[:-1]
    print answer
    
    s.PROMPT='Flag'
    s.sendline(answer)    
    s.prompt()
    ret = s.before.splitlines()
    print ret
  
if __name__ == '__main__':
    main()
