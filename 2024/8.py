import itertools

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def line(u: complex, v: complex, nrow: int, ncol: int) -> set:
	res = set()
	
	# First draw line in one direction
	z, d = u, u-v
	while (0 <= z.imag < ncol) and (0 <= z.real < nrow):
		res.add(z)
		z += d

	# Then the other
	z, d = v, v-u
	while (0 <= z.imag < ncol) and (0 <= z.real < nrow):
		res.add(z)
		z += d
	return res

def index_to_complex(index: int, ncol: int) -> complex:
	a, b = divmod(index, ncol)
	return a+b*1j

def part_1(puzzle_input: str) -> str:
	nrow = puzzle_input.count('\n')
	ncol = puzzle_input.index('\n')
	input_string = puzzle_input.replace('\n', '')
	frequencies = set(input_string) - {'.'}
	antinodes = set()
	for frequency in frequencies:
		indices = find_all(input_string, frequency)
		pairs = itertools.combinations(indices, 2)
		for pair in pairs:
			u, v = (index_to_complex(i, ncol) for i in pair)
			antinodes |= {2*u-v, 2*v-u}
	return len([node for node in antinodes if (0 <= node.imag < ncol) and (0 <= node.real < nrow)])
		
def part_2(puzzle_input: str) -> str:
	nrow = puzzle_input.count('\n')
	ncol = puzzle_input.index('\n')
	input_string = puzzle_input.replace('\n', '')
	frequencies = set(input_string) - {'.'}
	antinodes = set()
	for frequency in frequencies:
		indices = find_all(input_string, frequency)
		pairs = itertools.combinations(indices, 2)
		for pair in pairs:
			u, v = (index_to_complex(i, ncol) for i in pair)
			antinodes |= line(u, v, nrow, ncol)
	return len(antinodes)

def main():
	with(open('8.txt', 'r') as input_file):
		puzzle_input = input_file.read()
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	