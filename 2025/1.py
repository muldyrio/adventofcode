import numpy as np

def part_1(puzzle_input: str) -> int:
	turns = [50] + [int(d[1: ]) if d[0] == 'R' else -int(d[1: ]) for d in puzzle_input.split('\n')]
	return sum((np.cumsum(turns) % 100) == 0)

def part_2(puzzle_input: str) -> int:
	turns = [[1] * int(d[1:]) if d[0] == 'R' else [-1] * int(d[1:]) for d in puzzle_input.split('\n')]
	turns = [50] + [n for block in turns for n in block]
	return sum((np.cumsum(turns) % 100) == 0)

def main():
	with(open('1.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	