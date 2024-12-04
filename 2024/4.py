import numpy as np

# Thanks to Karl Knechtel on SO!
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


def n_xmas(index: tuple, string: str, ncol: int, nrow: int) -> int:
	i, j = index
	comp_strings = []

	if j <= ncol-4:
		comp_strings.append(string[i*nrow+j:i*nrow+j+4])
	if j <= ncol-4 and i <= nrow-4:
		comp_strings.append(string[i*nrow+j] + string[(i+1)*nrow+j+1] + string[(i+2)*nrow+j+2] + string[(i+3)*nrow+j+3])
	if i <= nrow-4:
		comp_strings.append(string[i*nrow+j] + string[(i+1)*nrow+j] + string[(i+2)*nrow+j] + string[(i+3)*nrow+j])
	if j >= 3 and i <= nrow-4:
		comp_strings.append(string[i*nrow+j] + string[(i+1)*nrow+(j-1)] + string[(i+2)*nrow+(j-2)] + string[(i+3)*nrow+(j-3)])
	if j >= 3:
		comp_strings.append(string[i*nrow+j:i*nrow+(j-4):-1])
	if i >= 3 and j >= 3:
		comp_strings.append(string[i*nrow+j] + string[(i-1)*nrow+(j-1)] + string[(i-2)*nrow+(j-2)] + string[(i-3)*nrow+(j-3)])
	if i >= 3:
		comp_strings.append(string[i*nrow+j] + string[(i-1)*nrow+j] + string[(i-2)*nrow+j] + string[(i-3)*nrow+j])
	if i >= 3 and j <= ncol-4:
		comp_strings.append(string[i*nrow+j] + string[(i-1)*nrow+(j+1)] + string[(i-2)*nrow+(j+2)] + string[(i-3)*nrow+(j+3)])

	return comp_strings.count('XMAS')

def is_x_mas(index: tuple, string: str, ncol: int, nrow: int) -> int:
	i, j = index
	if i in {0, nrow-1} or j in {0, ncol-1}:
		return False
	
	test_string = string[(i+1)*nrow+(j+1)] + string[(i+1)*nrow+(j-1)] + string[(i-1)*nrow+(j-1)] + string[(i-1)*nrow+(j+1)]
	return test_string in {'MSSM', 'SMMS', 'MMSS', 'SSMM'}
	

def part_1(puzzle_input: str) -> str:
	ncol = puzzle_input.index('\n')
	nrow = puzzle_input.count('\n') # there's always a trailing \n, so no need to add 1 for the first row
	
	puzzle_string = puzzle_input.replace('\n', '')
	x_indices = (divmod(k, ncol) for k in find_all(puzzle_string, 'X'))
	return sum(n_xmas(index, puzzle_string, ncol, nrow) for index in x_indices)

def part_2(puzzle_input: str) -> str:
	ncol = puzzle_input.index('\n')
	nrow = puzzle_input.count('\n')
	
	puzzle_string = puzzle_input.replace('\n', '')
	a_indices = (divmod(k, ncol) for k in find_all(puzzle_string, 'A'))
	return sum(is_x_mas(index, puzzle_string, ncol, nrow) for index in a_indices)

def main():
	with(open('4.txt', 'r') as input_file):
		puzzle_input = input_file.read()
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	