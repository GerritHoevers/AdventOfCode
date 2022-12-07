import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    data = [
    sum([
        int(cal)
        for cal in deer.split('\n')
        if cal != ''
    ])
    for deer in puzzle_input.split('\n\n')
    ]   
    return data

def part1(data):
    """Solve part 1"""
    return max(data)

def part2(data):
    """Solve part 2"""
    return sum(sorted(data)[-3:])

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
