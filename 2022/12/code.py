#--- Day 12: Hill Climbing Algorithm ---

import pathlib
import sys
import numpy as np
import time
from datetime import datetime


'''
Original code for finding the shortest path in a maze taken from:
https://www.techiedelight.com/find-shortest-path-in-maze/
With kind regards!
'''

# Check if it is possible to go to (x, y) from the current position. The
# function returns false if the cell is invalid, has value 0 or already visited
def isSafe(mat, visited, x_old, y_old, x, y, dist, min_dist):
	# break whem dist > min_dist
	if dist > min_dist:
		return False

	x_max = mat.shape[0]
	y_max = mat.shape[1]

	#print("checking move from ", x_old, y_old, "to ", x, y)

	if x < 0 or x >= x_max or y < 0 or y >= y_max:
		#print("out of bounds")
		return False
	if visited[x][y]:
		#print("visited")
		return False
	if ord(mat[x, y]) - ord(mat[x_old, y_old]) > 1 or ord(mat[x, y]) - ord(mat[x_old, y_old]) < 0:
		#print("step to big or step down")
		return False
	else:
		#print("step is ok")
		return True

# Find the shortest possible route in a matrix `mat` from source cell (i, j)
# to destination cell `dest`.

# `min_dist` stores the length of the shortest path from source to a destination
# found so far, and `dist` maintains the length of the path from a source cell to
# the current cell (i, j).

def findShortestPath(mat, visited, i, j, dest, min_dist=sys.maxsize, dist=0):

	#print("now at ", i, j, "char: ", mat[i, j])
	print(mat[i, j], end=" ")
	#time.sleep(1)
	# if the destination is found, update `min_dist`
	#print("compare ", i, j, "with ", dest)
	if [i, j] == dest:
		print("found!", "dist ", dist, "min_dist ", min_dist)
		return min(dist, min_dist)

	# set (i, j) cell as visited
	visited[i][j] = 1

	# go to the bottom cell
	if isSafe(mat, visited, i, j, i + 1, j, dist, min_dist):
		min_dist = findShortestPath(mat, visited, i + 1, j, dest, min_dist, dist + 1)

	# go to the right cell
	if isSafe(mat, visited, i, j, i, j + 1, dist, min_dist):
		min_dist = findShortestPath(mat, visited, i, j + 1, dest, min_dist, dist + 1)

	# go to the top cell
	if isSafe(mat, visited, i, j, i - 1, j, dist, min_dist):
		min_dist = findShortestPath(mat, visited, i - 1, j, dest, min_dist, dist + 1)

	# go to the left cell
	if isSafe(mat, visited, i, j, i, j - 1, dist, min_dist):
		min_dist = findShortestPath(mat, visited, i, j - 1, dest, min_dist, dist + 1)

	# backtrack: remove (i, j) from the visited matrix
	visited[i][j] = 0

	return min_dist

# Wrapper over findShortestPath() function
def findShortestPathLength(mat, src, dest):
	rows = mat.shape[0]

	# get source cell (i, j)
	i, j = src
	print("start: ", src)

	# get destination cell (x, y)
	x, y = dest
	print("finish: ", dest)

	# base case
	if rows == 0:
		return -1

	# `M × N` matrix
	(M, N) = (mat.shape[0], mat.shape[1])

	# construct an `M × N` matrix to keep track of visited cells
	visited = [[False for _ in range(N)] for _ in range(M)]

	min_dist = findShortestPath(mat, visited, i, j, dest)
	print("min_dist:", min_dist)

	if min_dist != sys.maxsize:
		return min_dist
	else:
		return -1


def parse(puzzle_input):
	"""Parse input"""

	lines = [text for text in puzzle_input.split('\n')]
	grid = np.matrix([list(line.strip()) for line in lines])
	# dimensions of the grid
	rows = grid.shape[0]
	cols = grid.shape[1]

	# find start- and finish-position
	start = []
	finish = []
	for row in range(rows):
		for col in range(cols):
			ch = grid[row, col]
			if ch == 'S':
				start = [row, col]
				grid[row, col] = 'a'
			elif ch == 'E':
				finish = [row, col]
				grid[row, col] = 'z'

	start = [10, 42]

	return grid, start, finish

def part1(grid, start, finish):
	"""Solve part 1"""
	print("\nsolving part 1 ...")

	return findShortestPathLength(grid, start, finish)

def part2(grid, start, finish):
	"""Solve part 2"""
	print("\nsolving part 2 ...")

	return


def solve(puzzle_input):
	"""Solve the puzzle for the given input"""
	grid, start, finish = parse(puzzle_input)

	solution1 = part1(grid, start, finish)
	solution2 = part2(grid, start, finish)

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
