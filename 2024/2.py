from typing import Generator

def diff(iterable: Generator) -> list:
	last = next(iterable)
	current = next(iterable)
	out = [current - last]
	for n in iterable:
		last = current
		current = n
		out.append(current - last)
	return out

def is_safe(instruction: Generator) -> bool:
	diffs = diff(instruction)
	return all(-3 <= d <= -1 for d in diffs) or all(1 <= d <= 3 for d in diffs)

def is_safe_dampened(instruction: Generator) -> bool:
	instruction_list = list(instruction)
	configs = [iter(instruction_list)] + [iter(instruction_list[:i] + instruction_list[i+1:]) for i in range(len(instruction_list))]
	return any(is_safe(c) for c in configs)

def part_1(puzzle_input: str) -> str:
	instructions = [(int(n) for n in d.split(' ')) for d in puzzle_input.split('\n')[:-1]]
	return sum(map(is_safe, instructions))

def part_2(puzzle_input: str) -> str:
	instructions = [(int(n) for n in d.split(' ')) for d in puzzle_input.split('\n')[:-1]]
	return sum(map(is_safe_dampened, instructions))

def main():
	with(open('2.txt', 'r') as input_file):
		puzzle_input = input_file.read()
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	