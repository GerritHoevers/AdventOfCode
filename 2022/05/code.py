# --- Day 5: Supply Stacks ---

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    stacks = [[]]
    for i in range(8):
        stacks.append([])
    moves = [[]]
    lines = [line for line in puzzle_input.split('\n')]
    line_number = 0
    stack_number = 0
    pos = 1
    value = lines[line_number][pos]
    while value != '1':
        #reading stack data
        if value != ' ':
            #there is a value on this position
            print("stack_number: ", stack_number, "value: ", value)
            stacks[stack_number].append(value)
        pos += 4
        stack_number += 1
        if pos > len(lines[line_number]):
            pos = 1
            stack_number = 0
            line_number += 1
        value = lines[line_number][pos]
    # reverse items in the stacks
    print("Na het inlezen zijn er ", len(stacks), " stacks")
    for i in range(0, len(stacks)):
        stacks[i].reverse()

    #arriving at the line with the stack numbers 
    line_number += 2 #skip 2 lines
    move_number = 0
    while line_number < len(lines):
        values = [value for value in lines[line_number].split(' ')]
        #print(values)
        moves[move_number].append(values[1])
        moves[move_number].append(values[3])
        moves[move_number].append(values[5])
        #print("move_number: ", move_number, "is ", moves[move_number])
        line_number += 1
        move_number += 1
        moves.append([])

    return stacks, moves

def part1(data):
    """Solve part 1"""
    print("solving part 1 ...")
    stacks, moves = data
    #print("moves: ", moves)
    #print("number of moves: ", len(moves))
    for i in range(0, len(moves)-1):
        print("stacks before move: ", stacks)
        number_to_move = int(moves[i][0])
        from_staple = int(moves[i][1]) - 1 #in code stapels are numbered starting with 0
        to_staple = int(moves[i][2]) - 1    
        print("move ", number_to_move, " from ", from_staple + 1, " to ", to_staple + 1)
        for j in range(0, number_to_move):
            stacks[to_staple].append(stacks[from_staple].pop())
        print("stacks after move: ", stacks)

    solution = ''
    print("Er zijn ", len(stacks), " stapels")
    for i in range(0,len(stacks)):
        print("stack number: ", i, "inhoud is: ", stacks[i], " lengte is: ", len(stacks[i]))
        text = stacks[i][len(stacks[i])-1]
        print(" last digit is: ", text)
        solution += text
    return solution

def part2(data):
    """Solve part 2"""
    print("\n\nsolving part 2 ...")
    stacks, moves = data
    #print("moves: ", moves)
    #print("number of moves: ", len(moves))
    for i in range(0, len(moves)-1):
        print("stacks before move: ", stacks)
        number_to_move = int(moves[i][0])
        from_staple = int(moves[i][1]) - 1 #in code stapels are numbered starting with 0
        to_staple = int(moves[i][2]) - 1    
        print("move ", number_to_move, " from ", from_staple + 1, " to ", to_staple + 1)        
        for j in range(number_to_move, 0, -1):
            print("from_staple is ", stacks[from_staple], " with length ", len(stacks[from_staple]))
            k = len(stacks[from_staple])-j
            print("now getting nr ", k, " from staple ", from_staple + 1)
            stacks[to_staple].append(stacks[from_staple].pop(k) )
        
        print("stacks after move: ", stacks)

    solution = ''
    print("Er zijn ", len(stacks), " stapels")
    for i in range(0,len(stacks)):
        print("stack number: ", i, "inhoud is: ", stacks[i], " lengte is: ", len(stacks[i]))
        text = stacks[i][len(stacks[i])-1]
        print(" last digit is: ", text)
        solution += text
    return solution

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
