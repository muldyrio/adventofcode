from functools import cache

@cache
def n_stones(num: int, n_blinks: int) -> int:
	if n_blinks == 1:
		return 2-(len(str(num)) % 2)

	if num == 0:
		return n_stones(1, n_blinks-1)

	num_str = str(num)
	l = len(num_str)
	if l % 2 == 0:
		return n_stones(int(num_str[:l // 2]), n_blinks-1) + n_stones(int(num_str[l // 2:]), n_blinks-1)
	
	return n_stones(2024 * num, n_blinks-1)

def part_1(puzzle_input: str) -> int:
	stones = map(int, puzzle_input.split(' '))
	return sum(map(lambda s: n_stones(s, 25), stones))

def part_2(puzzle_input: str) -> int:
	stones = map(int, puzzle_input.split(' '))
	return sum(map(lambda s: n_stones(s, 75), stones))

def main():
	with(open('11.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	