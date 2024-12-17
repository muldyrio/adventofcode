import re

def execute_instruction(ptr: int, ins: int, opr: int, reg: list, out: list) -> int:
	match ins:
		case 0:
			reg[4] = reg[4] // (2 ** reg[opr])
		case 1:
			reg[5] = reg[5] ^ opr
		case 2:
			reg[5] = reg[opr] % 8
		case 3:
			if reg[4] != 0:
				return opr
		case 4:
			reg[5] = reg[5] ^ reg[6]
		case 5:
			out.append(reg[opr] % 8)
		case 6:
			reg[5] = reg[4] // (2 ** reg[opr])
		case 7:
			reg[6] = reg[4] // (2 ** reg[opr])
	return ptr + 2

def execute_program(A: int, B: int, C: int, program: list) -> list:
	reg = [0, 1, 2, 3, A, B, C]
	out = []
	ptr = 0
	while ptr < len(program):
		ins, opr = program[ptr:ptr+2]
		ptr = execute_instruction(ptr, ins, opr, reg, out)
	return out

def checksum(A_lst: list, program: list) -> list:
	A = sum(d * 8 ** n for n, d in enumerate(A_lst))
	return execute_program(A, 0, 0, program)

def part_1(puzzle_input: str) -> str:
	A, B, C = map(int, re.findall(r'Register [ABC]: (\d+)', puzzle_input))
	program = list(map(int, re.findall(r'Program: ((?:\d,?)+)', puzzle_input)[0].split(',')))
	output = execute_program(A, B, C, program)
	return ','.join(map(str, output))

def part_2(puzzle_input: str) -> int:
	_, B, C = map(int, re.findall(r'Register [ABC]: (\d+)', puzzle_input))
	program = list(map(int, re.findall(r'Program: ((?:\d,?)+)', puzzle_input)[0].split(',')))
	N = len(program)
	good_progs = [[0] * N]
	for n in range(N-1, -1, -1):
		new_progs = []
		for prog in good_progs:
			for d in range(int(n == (N-1)), 8):
				new = prog[:]
				new[n] = d
				if checksum(new, program)[n] == program[n]:
					new_progs.append(new)
		good_progs = new_progs
	
	A_vals = map(lambda x: sum(d * 8 ** n for n, d in enumerate(x)), good_progs)
	return min(A_vals)

def main():
	with(open('17.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()