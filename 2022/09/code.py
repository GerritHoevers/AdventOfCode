#--- Day 9: Rope Bridge ---

import pathlib
import sys
import numpy as np
import math

def parse(puzzle_input):
    """Parse input"""

    return [text for text in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""
    print("\n\nsolving part 1 ...")

    def magnitude(vector):
        return math.sqrt(sum(pow(element, 2) for element in vector))

    def update(pH, pT):
        vec = pH - pT
        if (vec[0] == -1 and vec[1] == 2) or (vec[0] == -2 and vec[1] == 1):
            pT[0] -= 1
            pT[1] += 1
        elif (vec[0] == 1 and vec[1] == 2) or (vec[0] == 2 and vec[1] == 1):
            pT[0] += 1
            pT[1] += 1
        elif (vec[0] == 1 and vec[1] == -2) or (vec[0] == 2 and vec[1] == -1):
            pT[0] += 1
            pT[1] -= 1
        elif (vec[0] == -1 and vec[1] == -2) or (vec[0] == -2 and vec[1] == -1):
            pT[0] -= 1
            pT[1] -= 1
        elif (vec[0] == 0 and vec[1] == 2):
            pT[1] += 1
        elif (vec[0] == 2 and vec[1] == 0):
            pT[0] += 1
        elif (vec[0] == 0 and vec[1] == -2):
            pT[1] -= 1
        elif (vec[0] == -2 and vec[1] == 0):
            pT[0] += -1
        return pT

    posH = np.array([0, 0])
    posT = np.array([0, 0])
    positions = []

    for line in data:
        command = []
        command.append(line[0])
        command.append(int(line[1:]))
        
        dir = command[0]
        dist = command[1]

        if dir == 'L':
            for i in range(0, dist):
                posH[0] -= 1
                posT = update(posH, posT)
                print(posH, posT)
        
        elif dir == 'U':
            for i in range(0, dist):
                posH[1] += 1
                posT = update(posH, posT)
                print(posH, posT)

        elif dir == 'R':
            for i in range(0, dist):
                posH[0] += 1
                posT = update(posH, posT)
                print(posH, posT)

        elif dir == 'D':
            for i in range(0, dist):
                posH[1] -= 1
                posT = update(posH, posT)
                print(posH, posT)

    return len(positions)

def part2(data):
    """Solve part 2"""
    print("\n\nsolving part 2 ...")

    

    return
    
def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    print(data)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
