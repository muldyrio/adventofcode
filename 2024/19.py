from functools import cache

@cache
def is_possible(pattern: str, towels: tuple) -> bool:
	if pattern in towels:
		return True
	
	sub_patterns = set()
	for towel in towels:
		l = len(towel)
		if pattern[:l] == towel:
			sub_patterns.add(pattern[l:])

	return any(is_possible(sub_pattern, towels) for sub_pattern in sub_patterns)

@cache 
def n_possibilities(pattern: str, towels: tuple) -> int:
	out = 0
	if pattern in towels:
		out = 1
	
	sub_patterns = []
	for towel in towels:
		l = len(towel)
		if pattern[:l] == towel:
			sub_patterns.append(pattern[l:])
	
	return out + sum(n_possibilities(sub_pattern, towels) for sub_pattern in sub_patterns)


def part_1(puzzle_input: str) -> int:
	towels, patterns = puzzle_input.split('\n\n')
	towels = towels.split(', ')
	towels = tuple(sorted(towels, key=len))
	patterns = patterns.split('\n')
	return sum(is_possible(pattern, towels) for pattern in patterns)

def part_2(puzzle_input: str) -> int:
	towels, patterns = puzzle_input.split('\n\n')
	towels = towels.split(', ')
	towels = tuple(sorted(towels, key=len))
	patterns = patterns.split('\n')
	return sum(n_possibilities(pattern, towels) for pattern in patterns)


def main():
	with(open('19.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	