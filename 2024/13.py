import re

def get_pars(machine: str, part_2: bool=False) -> tuple:
	pattern = r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)'
	pars = [int(d) for d in re.findall(pattern, machine)[0]]
	if part_2:
		pars[4], pars[5] = pars[4] + 10000000000000, pars[5] + 10000000000000
	return pars

def is_solvable(x_A: int, y_A: int, x_B: int, y_B: int, x_P: int, y_P: int) -> bool:
	d = x_A*y_B-x_B*y_A
	if d == 0:
		print('Ping!')
		return False
	
	n_A = y_B*x_P-x_B*y_P
	n_B = x_A*y_P-y_A*x_P
	return (n_A % d == 0) and (n_B % d == 0)

def get_price(x_A: int, y_A: int, x_B: int, y_B: int, x_P: int, y_P: int) -> int:
	d = x_A*y_B-x_B*y_A
	n_A = y_B*x_P-x_B*y_P
	n_B = x_A*y_P-y_A*x_P
	return 3 * n_A // d + n_B // d

def part_1(puzzle_input: str) -> int:
	machines = puzzle_input.split('\n\n')
	price_total = 0
	for machine in machines:
		pars = get_pars(machine)
		if is_solvable(*pars):
			price_total += get_price(*pars)
	return price_total

def part_2(puzzle_input: str) -> int:
	machines = puzzle_input.split('\n\n')
	price_total = 0
	for machine in machines:
		pars = get_pars(machine, part_2=True)
		if is_solvable(*pars):
			price_total += get_price(*pars)
	return price_total

def main():
	with(open('13.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	