def concat(a: int, b: int) -> int:
	return int(str(a) + str(b))

def deconcat(a: int, b:int) -> int:
	a_str = str(a)
	b_str = str(b)
	return int(a_str[:-len(b_str)]) 

def is_concat(a: int, b: int) -> bool:
	if a == b:
		return False
	a_str = str(a)
	b_str = str(b)
	return a_str[-len(b_str):] == b_str 

def is_valid(target: int, inputs: list) -> bool:
	if len(inputs) == 2:
		return (target == inputs[0] + inputs[1]) or (target == inputs[0] * inputs[1])
	
	valid = is_valid(target - inputs[-1], inputs[:-1])
	if target % inputs[-1] == 0:
		valid = valid or is_valid(target // inputs[-1], inputs[:-1])
	
	return valid

def is_valid_concat(target: int, inputs: list) -> bool:
	if len(inputs) == 2:
		return (target == inputs[0] + inputs[1]) or (target == inputs[0] * inputs[1]) or (target == concat(*inputs))
	
	valid = is_valid_concat(target - inputs[-1], inputs[:-1])
	if target % inputs[-1] == 0:
		valid = valid or is_valid_concat(target // inputs[-1], inputs[:-1])
	if is_concat(target, inputs[-1]):
		valid = valid or is_valid_concat(deconcat(target, inputs[-1]), inputs[:-1])
	return valid

def part_1(puzzle_input: str) -> str:
	lines = puzzle_input[:-1].split('\n')
	equations = [(int(d.split(': ')[0]), [int(m) for m in d.split(': ')[1].split(' ')]) for d in lines]
	result = 0
	for equation in equations:
		if is_valid(*equation):
			result += equation[0]

	return result

def part_2(puzzle_input: str) -> str:
	lines = puzzle_input[:-1].split('\n')
	equations = [(int(d.split(': ')[0]), [int(m) for m in d.split(': ')[1].split(' ')]) for d in lines]
	result = 0
	for equation in equations:
		if is_valid_concat(*equation):
			result += equation[0]

	return result

def main():
	with(open('7.txt', 'r') as input_file):
		puzzle_input = input_file.read()
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	