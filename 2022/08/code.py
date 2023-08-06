#--- Day 8: Treetop Tree House ---

import pathlib
import sys
import numpy as np
from colorama import Cursor

def parse(puzzle_input):
    """Parse input"""

    lines = [text for text in puzzle_input.split('\n')]
    size = len(lines)
    grid = np.zeros((size, size)) #initialise grid with zeros
    
    #fill grid with data from input file
    row = 0
    for line in lines:
        for col in range(0, len(line)):
            num = int(line[col])
            grid[row][col] = num   
        row += 1

    return grid
    
def part1(grid):
    """Solve part 1"""
    print("\nsolving part 1 ...\n")

    dim = len(grid[0])
    visible_trees = 4*dim - 4

    for row in range(1, dim-1):
        for col in range(1, dim-1):
            #check view from left
            visible_from_left = True
            for j in range(0,col):
                if grid[row][j] >= grid[row][col]:
                    visible_from_left = False 
            #check view from top
            visible_from_top = True
            for i in range(0, row):
                if grid[i][col] >= grid[row][col]:
                    visible_from_top = False 
            #check view from right
            visible_from_right = True
            for j in range(col+1, dim):
                if grid[row][j] >= grid[row][col]:
                    visible_from_right = False 
            #check view from bottom
            visible_from_bottom = True
            for i in range(row+1, dim):
                if grid[i][col] >= grid[row][col]:
                    visible_from_bottom = False 

            if visible_from_left or visible_from_top or visible_from_right or visible_from_bottom:
                visible_trees += 1

    return visible_trees

def part2(grid):
    """Solve part 2"""
    print("\n\nsolving part 2 ...")

    dim = len(grid[0])
    
    max_scenic_score = 0

    for row in range(1, dim-1):
        for col in range(1, dim-1):

            #check view from left
            visible_from_left = 0
            for j in range(col-1, -1, -1):
                visible_from_left += 1
                if grid[row][j] >= grid[row][col]:
                    break
            
            #check view from top
            visible_from_top = 0
            for i in range(row-1 ,-1 , -1):
                visible_from_top += 1
                if grid[i][col] >= grid[row][col]:
                    break
                 
            #check view from right
            visible_from_right = 0
            for j in range(col+1, dim):
                visible_from_right += 1
                if grid[row][j] >= grid[row][col]:
                    break

            #check view from bottom
            visible_from_bottom = 0
            for i in range(row+1, dim):
                visible_from_bottom += 1
                if grid[i][col] >= grid[row][col]:
                    break

            scenic_score = visible_from_left * visible_from_top * visible_from_right * visible_from_bottom
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score

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
