#--- Day 8: Treetop Tree House ---

import pathlib
import sys
import numpy as np
from colorama import Cursor

def parse(puzzle_input):
    """Parse input"""

    lines = [text for text in puzzle_input.split('\n')]
    size = len(lines)
    print('size = ', size)
    grid = np.array
        
    for row in range(0, size):
        for col in range(0, size):
            tree_size = lines[row][col]
            print('row, col: ', row, col, tree_size)
            grid[row][col] = int(tree_size)
    
    print(grid)
    return grid

def part1(data):
    """Solve part 1"""
    print("\n\nsolving part 1 ...")


def part2(data):
    """Solve part 2"""
    print("\n\nsolving part 2 ...")

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
