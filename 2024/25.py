import numpy as np
from itertools import product

def translate(keylock: str, key=False) -> tuple:
	mat = np.array([list(d) for d in keylock.split('\n')[1:]])
	return tuple(np.count_nonzero(c == '#')-int(key) for c in np.transpose(mat))

def fits(key: tuple, lock: tuple) -> bool:
	for k, l in zip(key, lock):
		if k+l > 5:
			return False
	return True

def part_1(puzzle_input: str) -> int:
	lock_keys = puzzle_input.split('\n\n')
	keys = [translate(k, True) for k in lock_keys if k[:5] == '.....']
	locks = [translate(l) for l in lock_keys if l[:5] == '#####']
	return sum(fits(*keylock) for keylock in product(keys, locks))


def part_2(puzzle_input: str) -> int:
	pass

def main():
	with(open('25.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	