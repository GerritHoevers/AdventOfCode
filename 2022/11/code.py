#--- Day 11: Monkey in the Middle ---

import pathlib
import sys
import copy
from datetime import datetime

lcm = 9699690
class Monkey:
    def __init__(self, num, items, func, divisor, pass_if_true, pass_if_false):
        self.inspections = 0
        self.num = num
        self.items = items
        self.func = func
        self.divisor = divisor
        self.pass_if_true = pass_if_true
        self.pass_if_false = pass_if_false

def parse(puzzle_input):
    """Parse input"""

    data = [text for text in puzzle_input.split('\n')]

    #read in monkey data
    monkeys = []
    line_nr = 0
    while line_nr < len(data):
        text = data[line_nr]
        num = int(text[7])
        line_nr += 1
        text = data[line_nr]
        items = [ int(i) for i in (text[17:].split(",")) ]
        line_nr += 1
        text = data[line_nr]
        func = text[19:]
        line_nr += 1
        text = data[line_nr]
        divisor = int(text[21:])
        line_nr += 1
        text = data[line_nr]
        pass_if_true = int(text[29:])
        line_nr += 1
        text = data[line_nr]
        pass_if_false = int(text[30:])

        monkey = Monkey(num, items, func, divisor, pass_if_true, pass_if_false)
        monkeys.append(monkey)

        line_nr += 2

    return monkeys

def part1(data):
    """Solve part 1"""
    print("\nsolving part 1 ...")

    monkeys = copy.deepcopy(data)

    for round in range(20):
        print("round: ", round+1)
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections += 1
                old = item
                new = (eval(monkey.func) // 3)
                if new % monkey.divisor == 0:
                    new_monkey = monkey.pass_if_true
                else:
                    new_monkey = monkey.pass_if_false
                monkeys[new_monkey].items.append(new)
            monkey.items = []

    list_of_inspections = []
    for monkey in monkeys:
        num = monkey.inspections
        list_of_inspections.append(num)

    list_of_inspections.sort(reverse=True)
    print(list_of_inspections)

    return list_of_inspections[0] * list_of_inspections[1]

def part2(data):
    """Solve part 2"""
    print("\nsolving part 2 ...")

    monkeys = copy.deepcopy(data)

    for round in range(10000):
        print("round: ", round+1)
        for monkey in monkeys:
            for item in monkey.items:
                old_monkey = monkey.num
                monkey.inspections += 1
                old = item
                new = eval(monkey.func)

                if new % monkey.divisor == 0:
                        new_monkey = monkey.pass_if_true
                else:
                    new_monkey = monkey.pass_if_false

                new = new % lcm
                monkeys[new_monkey].items.append(new)
            monkey.items = []

    list_of_inspections = []
    for monkey in monkeys:
        num = monkey.inspections
        list_of_inspections.append(num)

    print(list_of_inspections)    
    list_of_inspections.sort(reverse=True)
    print(list_of_inspections)

    return list_of_inspections[0] * list_of_inspections[1]
    
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