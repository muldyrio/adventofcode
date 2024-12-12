from itertools import combinations

def pad(box: str) -> str:
	ncol = box.index('\n')
	out = '.' * (ncol + 2)
	for row in box.split('\n'):
		out += '\n.' + row + '.'
	out += '\n' + '.' * (ncol + 2)
	return out

def get_bed(i: int, plots: str, ncol: int) -> set:
	bed = {i}
	while True:
		border = set()
		for j in bed:
			border |= {j-1, j+1, j-ncol, j+ncol} - bed
		same_bed = {n for n in border if plots[n] == plots[i]}
		if not same_bed:
			return bed
		bed |= same_bed
	
def get_beds(plots: str) -> tuple:
	nrow = plots.count('\n') + 1
	ncol = plots.index('\n') + 1
	indices = ()
	for i in range(1, nrow-1):
		indices += tuple(range(i*ncol+1, (i+1)*ncol-2))
	beds = ()
	for i in indices:
		if not any(i in bed for bed in beds):
			beds += (get_bed(i, plots, ncol), )
	return beds

def get_perimeter(bed: set, ncol: int) -> int:
	perimeter = 0
	for i in bed:
		perimeter += 4 - len(bed.intersection({i-1, i+1, i-ncol, i+ncol}))
	return perimeter	

def n_corners(i: int, bed: set, ncol: int) -> int:
	neighbours = {i+1, i-1, i+ncol, i-ncol}.intersection(bed)
	
	if neighbours == set():
		return 4

	if len(neighbours) == 1:
		return 2
	
	if neighbours == {i+1, i-1} or neighbours == {i+ncol, i-ncol}:
		return 0
	
	if len(neighbours) == 2:
		return 2 - ((sum(neighbours) - i) in bed)
	
	corners = {sum(c)-i for c in combinations(neighbours, 2)} - {i}
	
	if len(neighbours) == 3:
		return 2 - len(corners.intersection(bed))

	return 4 - len(corners.intersection(bed))
	

def get_n_sides(bed: set, ncol: int) -> int:
	sides = 0
	for i in bed:
		sides += n_corners(i, bed, ncol)
	return sides

def part_1(puzzle_input: str) -> int:
	plots = pad(puzzle_input)
	beds = get_beds(plots)
	return sum(len(bed) * get_perimeter(bed, plots.index('\n')+1) for bed in beds)

def part_2(puzzle_input: str) -> int:
	plots = pad(puzzle_input)
	beds = get_beds(plots)
	return sum(len(bed) * get_n_sides(bed, plots.index('\n')+1) for bed in beds)

def main():
	with(open('12.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	