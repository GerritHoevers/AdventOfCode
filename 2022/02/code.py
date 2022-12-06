import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [strategy_for_round.split(' ') for strategy_for_round in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""


def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    #print("data: ", data)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        #print("puzzle_input: " , puzzle_input)
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
