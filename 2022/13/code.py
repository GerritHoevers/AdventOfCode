# --- Day 13: Distress Signal ---

import pathlib
import sys
from datetime import datetime


def get_elements(packet):
    # get list of elements in packet
    elements = []
    # skip leading '['
    index_packet = 1
    index = 0
    char = packet[index_packet]



    return elements

def parse(puzzle_input):
    """Parse input"""

    data = [text for text in puzzle_input.split('\n')]
    packets = []
    pair = 0
    while (pair*3) < len(data):
        packets.append(data[3*pair])
        packets.append(data[3*pair+1])
        pair += 1

    return packets

def part1(data):
    """Solve part 1"""
    print("\nsolving part 1 ...")

    pairs = len(data) // 2
    for i in range(pairs):
        left_packet = data[2*i]
        right_packet = data[2*i+1]
        print("== Pair", i+1, "==")
        print("- Compare", left_packet, " vs ", right_packet)
        left_elements = get_elements(left_packet)
        right_elements = get_elements(right_packet)
        for j in range(len(left_elements)):
            print("  - Compare", left_elements[j], "vs", right_elements[j])
        print()

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
