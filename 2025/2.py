def is_invalid(n: int, part_2: bool=False) -> bool:
	n_str = str(n)
	n_len = len(n_str)
	if part_2:
		for i in range(1, n_len // 2 + 1):
			if n_str == n_str[:i] * (n_len // i):
				return True
		return False

	if n_len % 2 == 1:
		return False
	
	return n_str[:n_len//2] == n_str[n_len//2:]

def part_1(puzzle_input: str) -> int:
	ranges = [range(int(d.split('-')[0]), int(d.split('-')[1])+1) for d in puzzle_input.split(',')]
	out = 0
	for r in ranges:
		out += sum(n for n in r if is_invalid(n))
	return out

def part_2(puzzle_input: str) -> int:
	ranges = [range(int(d.split('-')[0]), int(d.split('-')[1])+1) for d in puzzle_input.split(',')]
	out = 0
	for r in ranges:
		out += sum(n for n in r if is_invalid(n, True))
	return out

def main():
	with(open('2.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	