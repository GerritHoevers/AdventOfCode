#--- Day 7: No Space Left On Device ---

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [text for text in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""
    print("\n\nsolving part 1 ...")
    dirs = 0
    for line in data:
        if line[0:3] == "dir":
            dirs += 1
            print(dirs, line)

    return      

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
