#--- Day 10: Cathode-Ray Tube ---

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [text for text in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""
    print("\nsolving part 1 ...")

    cycle = 0
    x = 1
    signal_strengths = []
    signal_strengths.append(1) #signal strength index 0 not in use
    for line in data:
        code = line.split(' ')
        operation = code[0]
        cycle += 1
        signal_strengths.append(cycle * x)
        print("cycle:", cycle, "x_in:", x, "code:", code, "x_out:", x, "signal_strenght:", signal_strengths[cycle])
        if operation == 'addx':
            cycle += 1
            x_in = x
            x = x + int(code[1])
            signal_strengths.append(cycle * x_in)
            print("cycle:", cycle, "x_in:", x_in, "code:", code, "x_out:", x, "signal_strenght:", signal_strengths[cycle] )

    sum = 0
    for i in range(20, 260, 40):
        sum += signal_strengths[i]

    return sum

def part2(data):
    """Solve part 2"""
    print("\nsolving part 2 ...")

    cycle = 0
    x = 1
    crt = 0

    for line in data:
        code = line.split(' ')
        operation = code[0]
        cycle += 1
        x_in = x
        x_out = x_in
        char = "."
        if (x_in - 1) == crt or x_in == crt or x_in + 1 == crt:
            char = "#"
        #print("cycle:", cycle, "crt: ", crt, "x_in:", x_in, "code:", code, "x_out:", x_out, char)
        print(char, end="")
        crt += 1
        if crt > 39:
            crt = 0
            print()
        if operation == 'addx':
            cycle += 1
            x_in = x
            x = x + int(code[1])
            x_out = x
            char = "."
            if (x_in - 1) == crt or x_in == crt or x_in + 1 == crt:
                char = "#"
            #print("cycle:", cycle, "crt:", crt, "x_in:", x_in, "code:", code, "x_out:", x_out, char)
            print(char, end="")
            crt += 1
            if crt > 39:
                crt = 0
                print()
    print()

    return
    
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
