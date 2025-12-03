def get_max_joltage(bank: list[int], n_batteries: int) -> int:
	if n_batteries == 1:
		return max(bank)
	
	i_max = max(range(len(bank)-(n_batteries-1)), key=bank.__getitem__)
	return 10 ** (n_batteries-1) * bank[i_max] + get_max_joltage(bank[i_max+1:], n_batteries-1)

def part_1(puzzle_input: str) -> int:
	banks =  (list(map(int, list(d))) for d in puzzle_input.split('\n'))
	return sum(map(lambda bank: get_max_joltage(bank, 2), banks))

def part_2(puzzle_input: str) -> int:
	banks =  (list(map(int, list(d))) for d in puzzle_input.split('\n'))
	return sum(map(lambda bank: get_max_joltage(bank, 12), banks))

def main():
	with(open('3.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	