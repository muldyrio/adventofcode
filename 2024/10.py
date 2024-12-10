def get_neighbours(i: int, _map: str, ncol: int, nrow: int) -> list:
	out = []
	if i % ncol != 0:
		out.append(i-1)
	if (i+1) % ncol != 0:
		out.append(i+1)
	if i >= ncol:
		out.append(i-ncol)
	if i < (nrow-1)*ncol:
		out.append(i+ncol)
	return out

def reachable(i: int, j: int, _map: str, ncol: int, nrow: int) -> bool:
	neighbours = get_neighbours(j, _map, ncol, nrow)	
	if _map[j] == '1':
		return i in neighbours
	
	lower_neighbours = [n for n in neighbours if int(_map[n]) == (int(_map[j])-1)]
	return any((reachable(i, n, _map, ncol, nrow) for n in lower_neighbours))

def rating(i: int, j: int, _map: str, ncol: int, nrow: int) -> bool:
	neighbours = get_neighbours(j, _map, ncol, nrow)	
	if _map[j] == '1':
		return i in neighbours
	
	lower_neighbours = [n for n in neighbours if int(_map[n]) == (int(_map[j])-1)]
	return sum((rating(i, n, _map, ncol, nrow) for n in lower_neighbours))

def part_1(puzzle_input: str) -> str:
	nrow = puzzle_input.count('\n') + 1
	ncol = puzzle_input.index('\n')
	puzzle_input = puzzle_input.replace('\n', '')
	trailheads = [i for i, s in enumerate(puzzle_input) if s == '0']
	peaks = [i for i, s in enumerate(puzzle_input) if s == '9']
	score = 0
	for i in trailheads:
		for j in peaks:
			if reachable(i, j, puzzle_input, ncol, nrow):
				score += 1
	return score

def part_2(puzzle_input: str) -> str:
	nrow = puzzle_input.count('\n') + 1
	ncol = puzzle_input.index('\n')
	puzzle_input = puzzle_input.replace('\n', '')
	trailheads = [i for i, s in enumerate(puzzle_input) if s == '0']
	peaks = [i for i, s in enumerate(puzzle_input) if s == '9']
	score = 0
	for i in trailheads:
		for j in peaks:
			score += rating(i, j, puzzle_input, ncol, nrow)
	return score

def main():
	with(open('10.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	