# --- Day 5: Supply Stacks ---

import pathlib
import sys

staples = 3

def parse(puzzle_input):
    """Parse input"""
    data = []
    moves = []
    for line in puzzle_input.split('\n'):
        #print(line, len(line))
        index = 0
        row = 0
        symbol = line[index+1]
        if symbol !=1:
            # line contains crate data
            while index+3 < len(line) and symbol != ' ':
                print("index: ", index, "symbol: ", symbol, "row: ", row)
                data[row].append(symbol)
                index += 4
                row += 1
            else:
                break

    #data = [['Z', 'N'], ['M', 'C', 'D'], ['P'], [1,2,1], [3,1,3], [2,2,1], [1,1,2]]
    print(data)
    return data, moves

def part1(data):
    """Solve part 1"""
    rows = []
    for i in range(0, staples):
        rows.append(data[i]) 
    moves = []
    for i in range(staples, len(data)):
        moves.append(data[i]) 
    #print(moves)
    for i in range(0, len(moves)):
        number_to_move = moves[i][0]
        from_staple = moves[i][1] - 1
        to_staple = moves[i][2] - 1
        #print("move ", number_to_move, " from ", from_staple, " to ", to_staple)
        for j in range(0, number_to_move):
            rows[to_staple].append(rows[from_staple].pop())
        #print(rows)

    solution = ''
    for i in range(0,staples):
        text = rows[i][len(rows[i])-1]
        solution += text
    return solution

def part2(data):
    """Solve part 2"""


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
