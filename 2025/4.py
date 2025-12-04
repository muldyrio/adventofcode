import numpy as np
from itertools import product
from typing import Iterable

def get_neighbours(i: int, j: int, h: int, w: int) -> Iterable[tuple[int]]:
	dirs = np.array([[-1, -1], [-1,  0], [-1,  1],
					 [ 0, -1], [ 0,  1],
					 [ 1, -1], [ 1,  0], [ 1,  1]])
	candidates = dirs + np.array([i, j])
	return ((y, x) for (y, x) in candidates if 0 <= x < w and 0 <= y < h)

def is_movable(i: int, j: int, layout: np.array) -> bool:
	neighbours = get_neighbours(i, j, *layout.shape)
	return sum(layout[*d] for d in neighbours) < 4 and layout[i, j]

def part_1(puzzle_input: str) -> int:
	layout = np.array([np.asarray(list(d)) for d in puzzle_input.split('\n')]) == '@'
	return sum(is_movable(i, j, layout) for i, j in product(*map(range, layout.shape)))

def part_2(puzzle_input: str) -> int:
	layout = np.array([np.asarray(list(d)) for d in puzzle_input.split('\n')]) == '@'
	res = 0
	while True:
		moveable = [(i, j) for i, j in product(*map(range, layout.shape)) if is_movable(i, j, layout)]
		if not moveable:
			break
		res += len(moveable)
		for pos in moveable:
			layout[*pos] = False
	
	return res

def main():
	with(open('4.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	