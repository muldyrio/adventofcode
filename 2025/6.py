import re
from numpy import prod

def format_number(number: list[str]) -> list[int]:
	return [int(''.join(d).replace(' ', '')) for d in zip(*number)]

def solve_problem(problem: list[int, str]) -> int:
	if problem[-1] == '+':
		return sum(problem[:-1])
	return prod(problem[:-1])

def solution(puzzle_input: str) -> None:
	# Part 1
	numbers = list(map(int, re.findall(r'(\d+)', puzzle_input)))
	operations = re.findall(r'([\+\*])', puzzle_input)
	problems = [numbers[i::len(operations)] + [o] for i, o in enumerate(operations)]
	print(sum(map(solve_problem, problems)))

	# Part 2
	l1, l2, l3, l4, operations = puzzle_input.split('\n')
	problem_starts = [m.start(0) for m in re.finditer(r'[\*\+]', operations)]
	problem_ends = [s-1 for s in problem_starts[1:]] + [len(operations)]
	numbers = [[l1[l:u], l2[l:u], l3[l:u], l4[l:u]] for (l, u) in zip(problem_starts, problem_ends)]
	operations = re.findall(r'([\+\*])', puzzle_input)
	print(sum(map(solve_problem, (format_number(numbers[i]) + [o] for i, o in enumerate(operations)))))

def main():
	with(open('6.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		solution(puzzle_input)

if __name__ == '__main__':
	main()
	