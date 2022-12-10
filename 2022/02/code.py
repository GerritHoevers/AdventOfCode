# --- Day 2: Rock Paper Scissors ---

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [strategy_for_round.split(' ') for strategy_for_round in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""
    total_score = 0
    for choices in data:
        score = 0
        their_choice = choices[0]
        my_choice = choices[1]
        if my_choice == 'X':
            score +=1
            if their_choice == 'A':
                score += 3
            elif their_choice == 'B':
                score += 0
            else:
                #their_score is 'C':
                score += 6

        elif my_choice == 'Y':
            score += 2
            if their_choice == 'A':
                score += 6
            elif their_choice == 'B':
                score += 3
            else:
                score += 0
        else:
            #my_choice is 'Z'
            score += 3
            if their_choice == 'A':
                score += 0
            elif their_choice == 'B':
                score += 6
            else:
                score += 3
        total_score += score
    return total_score
        
def part2(data):
    """Solve part 2"""
    total_score = 0
    for choices in data:
        score = 0
        their_choice = choices[0]
        result = choices[1]
        if their_choice == 'A':
            if  result == 'X':
                score += 0 #loose
                score += 3 #Z
            elif result == 'Y':
                score += 3 #draw
                score += 1 #X
            else:
                #result is 'Z':
                score += 6 #win
                score += 2 #Y

        elif their_choice == 'B':
            if  result == 'X':
                score += 0 #loose
                score += 1 #X
            elif result == 'Y':
                score += 3 #draw
                score += 2 #Y
            else:
                #result is 'Z':
                score += 6 #win
                score += 3 #Z
        else:
            #their_choice is 'C'
            if  result == 'X':
                score += 0 #loose
                score += 2 #Y
            elif result == 'Y':
                score += 3 #draw
                score += 3 #Z
            else:
                #result is 'Z':
                score += 6 #win
                score += 1 #X

        total_score += score
        print('score, total_score', score, total_score)
    return total_score

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = pathlib.Path("input.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
