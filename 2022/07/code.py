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
    return [text for text in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""
    print("\n\nsolving part 1 ...")
    Folder_e = Folder('e', 'a')
    files = [ File(584, 'i', 'e') ]
    for file in files:
        Folder_e.children.append(file)

    Folder_a = Folder('a', '/')
    files = [ File(29116, 'f', 'a'), File(2557, 'g', 'a'),  File(62596, 'h.lst', 'a') ]
    for file in files:
        Folder_a.children.append(file)
    Folder_a.children.append(Folder_e)
    
    files =  [ File(4060174, 'j', 'd'), File(8033020, 'd.log', 'd'), 
        File(5626152, 'd.ext', 'd'), File(7214296, 'k', 'd') ]
    Folder_d = Folder( 'd', '/')
    for file in files:
        Folder_d.children.append(file)

    files =  [ File(14848514, 'b.txt', '/'), File(8504156, 'c.dat', '/') ]
    root = Folder("/", parent=None)
    for file in files:
        root.children.append(file)
    root.children.append(Folder_a)
    root.children.append(Folder_d)

    print("size of root: ", root.get_size())

    i = 0
    for child in root.children:
        i += 1
        if type(child) == Folder:
            print("child nr ", i, " dir: ", child.dirname, " size: ", child.get_size())
        else:
            print("child nr ", i, " file: ", child.filename, " size: ", child.get_size())

        
    return      

def part2(data):
    """Solve part 2"""
    print("\n\nsolving part 2 ...")


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