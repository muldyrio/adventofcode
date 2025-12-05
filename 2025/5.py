def collapse(ranges: list[list[int]]) -> list[list[int]]:
	ranges.sort(key=lambda r: r[0])
	i = 0
	while i < len(ranges):
		for r in ranges[i+1:]:
			if r[0] > ranges[i][1] + 1:
				break

			ranges[i][1] = max(ranges[i][1], r[1])
			ranges.remove(r)
		i += 1
	return ranges

def is_fresh(ID: int, ranges: list[list[int]]) -> bool:
	for r in ranges:
		if r[0] <= ID <= r[1]:
			return True
	return False

def solution(puzzle_input: str) -> None:
	# Process input
	ranges, IDs = puzzle_input.split('\n\n')
	ranges = collapse([list(map(int, r.split('-'))) for r in ranges.split('\n')])
	IDs = map(int, IDs.split('\n'))

	# Part 1
	print(sum(map(lambda ID: is_fresh(ID, ranges), IDs)))

	# Part 2
	print(sum(map(lambda r: r[1]-r[0]+1, ranges)))

def main():
	with(open('5.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		solution(puzzle_input)

if __name__ == '__main__':
	main()
	