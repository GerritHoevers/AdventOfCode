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

    def move(pH, pT):
        vec = [ pH[0] - pT[0], pH[1] - pT[1] ]
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

    posH = [0, 0]
    posT = [0, 0]
    positions = set()
    positions.add(tuple(posT))

    for line in data:
        dir = line[0]
        dist = int(line[1:])

        if dir == 'L':
            for i in range(0, dist):
                posH[0] -= 1
                posT = move(posH, posT)
                positions.add(tuple(posT))

        elif dir == 'U':
            for i in range(0, dist):
                posH[1] += 1
                posT = move(posH, posT)
                positions.add(tuple(posT))
                
        elif dir == 'R':
            for i in range(0, dist):
                posH[0] += 1
                posT = move(posH, posT)
                positions.add(tuple(posT))

        elif dir == 'D':
            for i in range(0, dist):
                posH[1] -= 1
                posT = move(posH, posT)
                positions.add(tuple(posT))

    return len(positions)

def part2(data):
    """Solve part 2"""
    print("\n\nsolving part 2 ...")

    def move(pH, pT):
        vec = [ pH[0] - pT[0], pH[1] - pT[1] ]
        if (vec[0] == -1 and vec[1] == 2) or (vec[0] == -2 and vec[1] == 1) or (vec[0] == -2 and vec[1] == 2):
            pT[0] -= 1
            pT[1] += 1
        elif (vec[0] == 1 and vec[1] == 2) or (vec[0] == 2 and vec[1] == 1)  or (vec[0] == 2 and vec[1] == 2):
            pT[0] += 1
            pT[1] += 1
        elif (vec[0] == 1 and vec[1] == -2) or (vec[0] == 2 and vec[1] == -1)  or (vec[0] == 2 and vec[1] == -2):
            pT[0] += 1
            pT[1] -= 1
        elif (vec[0] == -1 and vec[1] == -2) or (vec[0] == -2 and vec[1] == -1)  or (vec[0] == -2 and vec[1] == -2):
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

    dim = 10
    head = 0
    tail = dim - 1
    knots = []
    for i in range(dim):
        knots.append([0, 0])
    positions = set()
    positions.add(tuple(knots[tail]))

    for line in data:
        dir = line[0]
        dist = int(line[1:])

        if dir == 'L':
            for i in range(0, dist):
                knots[head][0] -= 1
                for i in range(1, dim):
                    knots[i] = move(knots[i-1], knots[i])
                positions.add(tuple(knots[tail]))

        elif dir == 'U':
            for i in range(0, dist):
                knots[head][1] += 1
                for i in range(1, dim):
                    knots[i] = move(knots[i-1], knots[i])
                positions.add(tuple(knots[tail]))
                                
        elif dir == 'R':
            for i in range(0, dist):
                knots[head][0] += 1
                for i in range(1, dim):
                    knots[i] = move(knots[i-1], knots[i])
                positions.add(tuple(knots[tail]))

        elif dir == 'D':
            for i in range(0, dist):
                knots[head][1] -= 1
                for i in range(1, dim):
                    knots[i] = move(knots[i-1], knots[i])
                positions.add(tuple(knots[tail]))

    return len(positions)
    
def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
