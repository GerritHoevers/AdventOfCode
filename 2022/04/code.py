# --- Day 4: Camp Cleanup ---

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [text for text in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""
    score = 0
    for text in data:
        t1 = text.split(',') #vb [2-4, 6-8]
        t2 = t1[0].split('-')
        t3 = t1[1].split('-')
        i1 = int(t2[0])
        i2 = int(t2[1])
        j1 = int(t3[0])
        j2 = int(t3[1])
        inRangeRinL = True
        for j in range(j1, j2+1):
            if j < i1 or j > i2:
                inRangeRinL = False
                break
        inRangeLinR = True
        for i in range(i1, i2+1):
            if i < j1 or i > j2:
                inRangeLinR = False
                break
        if inRangeRinL or inRangeLinR:
            score += 1

    return score

def part2(data):
    """Solve part 2"""
    total_overlap = 0
    for text in data:
        t1 = text.split(',') #vb [2-4, 6-8]
        t2 = t1[0].split('-')
        t3 = t1[1].split('-')
        i1 = int(t2[0])
        i2 = int(t2[1])
        j1 = int(t3[0])
        j2 = int(t3[1])
        overlapRL = False
        for j in range(j1, j2+1):
            if j >= i1 and j <= i2:
                overlapRL = True
                break
        overlapLR = False
        for i in range(i1, i2+1):
            if i >= j1 and i <= j2:
                overlapLR = True
                break
        if overlapRL or overlapLR:
            total_overlap += 1

    return total_overlap


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
