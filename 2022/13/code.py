# --- Day 13: Distress Signal ---

import pathlib
import sys
from datetime import datetime


def convert(text):
    # convert text to list of strings
    elements = []

    return elements

def parse(puzzle_input):
    """Parse input"""

    data = []
    pair = 0
    for text in puzzle_input.split('\n'):
        if text != "":
            data.append(text)



    return data

def part1(data):
    """Solve part 1"""
    print("\nsolving part 1 ...")

    #pairs = len(data)
    pairs = 1
    for i in range(pairs):
        left_packet = data[i][0]
        right_packet = data[i][1]
        print("== Pair", i+1, "==")
        print("- Compare ", left_packet, " vs ", right_packet)

    return

def part2(data):
    """Solve part 2"""
    print("\nsolving part 2 ...")

    return

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    now = datetime.now()
    start_time = now.strftime("%H:%M:%S")

    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

    now = datetime.now()
    end_time = now.strftime("%H:%M:%S")

    print("start time =", start_time)
    print("end time =", end_time)
