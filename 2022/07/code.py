#--- Day 7: No Space Left On Device ---

import pathlib
import sys

class Folder:
    def __init__(self, dirname, parent):
        self.dirname = dirname
        self.children = []
        self.parent = parent

    def get_size(self):
        return sum([child.get_size() for child in self.children])

class File:
    def __init__(self, size, filename, parent):
        self.size = size
        self.filename = filename
        self.parent = parent

    def get_size(self):
        return self.size

def parse(puzzle_input):
    """Parse input"""
    data = [text for text in puzzle_input.split('\n')]

    #create folder- and filestructure
    nodes = [] #list of all nodes
    root = Folder('/', parent=None)
    nodes.append(root)
    current_node = root
    line_number = 1 #skip line_number 0, it contains "$ cd /"
    
    while line_number < len(data):
        values = data[line_number].split(' ')
        #the first value is "ls" or "cd"
        if values[1] == 'ls':
            #the command is 'ls', what follows are zero or more lines with the content of current_node
            line_number += 1
            while line_number < len(data):
                #not reaching the end of the data
                values = data[line_number].split(' ')
                if values[0] == '$':
                    #no items in this folder, return to upper while loop
                    break
                else:
                    if values[0] == 'dir':
                        #a new dir
                        name = values[1]
                        folder = Folder(name, parent=current_node)
                        current_node.children.append(folder)
                        nodes.append(folder)
                    else:
                        #a new file
                        size = int(values[0])
                        name = values[1]
                        file = File(size, name, current_node)
                        current_node.children.append(file)
                line_number += 1
        else: 
            #command is 'cd', second value gives the name of the new dir, or '..' for shift ip
            dirname = values[2]
            if dirname == '..':
                #shft one dir up
                current_node = current_node.parent
            else:
                #look in children of current_node for the right subdirectory
                for item in current_node.children:
                    if type(item) == Folder:
                        if item.dirname == dirname:
                            #change current_node to this directory
                            current_node = item
            line_number += 1

    return nodes

def part1(nodes):
    """Solve part 1"""
    print("\n\nsolving part 1 ...")
    
    sum = 0
    for node in nodes:
        size = node.get_size()
        if size <= 100000:
            sum += size
    return sum
    
def part2(nodes):
    """Solve part 2"""
    print("\n\nsolving part 2 ...")

    total_used = nodes[0].get_size()
    free = 70000000 - total_used

    min_size = 70000000
    for node in nodes:
        size = node.get_size()
        if free + size >= 30000000:
            if size < min_size:
                min_size = size

    return min_size

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