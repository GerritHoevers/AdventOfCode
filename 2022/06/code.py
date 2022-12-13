#--- Day 6: Tuning Trouble ---

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    data = ''
    lines = [line for line in puzzle_input.split('\n')]
    for line in lines:
        data += line
    return data

def isMarker(t, len):
    if t[0] in t[1:len]:
        return False
    
    for i in range(1, len-1):
        if t[i] in (t[i-1] + t[i+1:len]):
            return False
    
    if t[len-1] in t[0:len-1]:
        return False

    return True

def part1(data):
    """Solve part 1"""
    print("\n\nsolving part 1 ...")
    index = 3
    marked = False
    while not marked:
        text = data[index-3:index+1]
        print(index, text)
        marked = isMarker(text, 4)
        index += 1
    return index

def part2(data):
    """Solve part 2"""
    print("\n\nsolving part 2 ...")
    index = 14
    marked = False
    while not marked:
        text = data[index-14:index+1]
        print(index, text)
        marked = isMarker(text, 14)
        index += 1
    return index

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