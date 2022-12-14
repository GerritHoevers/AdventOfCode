# --- Day 3: Rucksack Reorganization ---

import pathlib
import sys
from itertools import islice

def priority(i):
        if ord(i) < 91: #upper case
            return ord(i)-38
        else: #lower case
            return ord(i)-96

def parse(puzzle_input):
    """Parse input"""
    return [text for text in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""

    score = 0
    for text in data:
        l = int(len(text))
        l2 = int(l/2)
        text1 = text[0:l2]
        text2 = text[l2:l]
        
        break_loop = False
        for i in text1:
            for j in text2:
                if j == i:
                    score += priority(j)
                    break_loop = True
                    break
            if break_loop == True:
                break
        #i is the character we're looking for
        
        print(text, i, priority(i), score)
      
    return score

def part2(data):
    """Solve part 2"""

    score = 0
    num_of_sets = len(data) // 3
    print("number of sets: ", num_of_sets)
    for i in range(0, num_of_sets):
        list_of_three = [x.strip() for x in islice(data, i*3, i*3+3)]
        #print(list_of_three)
        
        break_loop = False
        for i in list_of_three[0]:
            for j in list_of_three[1]:
                for k in list_of_three[2]:
                    if i==j and j==k:
                        score += priority(k)
                        break_loop = True
                        break
                if break_loop == True:
                    break
            if break_loop == True:
                break

        print(list_of_three, i, priority(i), score)

    return score

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
