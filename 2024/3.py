import re

def part_1(puzzle_input: str) -> str:
	mult_instructions = re.findall(r'mul\((\d+),(\d+)\)', puzzle_input)
	return sum(map(lambda x: int(x[0]) * int(x[1]), mult_instructions))

def part_2(puzzle_input: str) -> str:
	mult_instructions = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", puzzle_input)
	res = 0
	do_mult = True

	for instruction in mult_instructions:
		x, y, do, dont = instruction
		if do:
			do_mult = True
		elif dont:
			do_mult = False
		else:
			if do_mult:
				res += int(x) * int(y)
	return res

def main():
	with(open('3.txt', 'r') as input_file):
		puzzle_input = input_file.read()

	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	