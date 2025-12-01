def sgn(x: int) -> int:
	return int(x >= 0) - int(x < 0)

def get_keypresses(code: str, numeric=False) -> str:
	if numeric:
		x, y = 2, 3
		x_dict = {'7': 0, '4': 0, '1': 0, '8': 1, '5': 1, '2': 1, '0': 1, '9': 2, '6': 2, '3': 2, 'A': 2}
		y_dict = {'7': 0, '4': 1, '1': 2, '8': 0, '5': 1, '2': 2, '0': 3, '9': 0, '6': 1, '3': 2, 'A': 3}
	else:
		x, y = 2, 0
		x_dict = {'<': 0, '^': 1, 'v': 1, 'A': 2, '>': 2}
		y_dict = {'<': 1, '^': 0, 'v': 1, 'A': 0, '>': 1}
	out_code = ''
	for char in code:
		new_x = x_dict[char]
		new_y = y_dict[char]
		dx, dy = new_x-x, new_y-y
		match (sgn(dx), sgn(dy)):
			case (-1, -1):
				out_code += '^' * (-dy) + '<' * (-dx)
			case (-1, 1):
				out_code += 'v' * dy + '<' * (-dx)
			case (1, -1):
				out_code += '^' * (-dy) + '>' * dx
			case (1, 1):
				out_code += '>' * dx + 'v' * dy
		out_code += 'A'
		x, y = new_x, new_y
	return out_code

def n_keypresses(code: str) -> int:
	numeric = get_keypresses(code, numeric=True)
	directional_1 = get_keypresses(numeric)
	directional_2 = get_keypresses(directional_1)
	print(numeric)
	print(directional_1)
	print(directional_2)
	return len(directional_2)

def part_1(puzzle_input: str) -> int:
	codes = (d for d in puzzle_input.split('\n'))
	for code in codes:
		print(int(code[:-1]), n_keypresses(code))
#	return sum(int(code[:-1]) * n_keypresses(code) for code in codes)	

def part_2(puzzle_input: str) -> int:
	pass

def main():
	with(open('21.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1('''379A'''))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	