def part_1(puzzle_input: str) -> str:
	num_pairs = [(int(d.split('   ')[0]), int(d.split('   ')[1])) for d in puzzle_input.split('\n')[:-1]]
	left_list = sorted([d[0] for d in num_pairs])
	right_list = sorted([d[1] for d in num_pairs])
	return sum(abs(l-r) for l, r in zip(left_list, right_list))
	
def part_2(puzzle_input: str) -> str:
	num_pairs = [(int(d.split('   ')[0]), int(d.split('   ')[1])) for d in puzzle_input.split('\n')[:-1]]
	left_list = (d[0] for d in num_pairs)
	right_list = [d[1] for d in num_pairs]
	
	out = 0
	for l in left_list:
		out += l * right_list.count(l)
	return out
	

def main():
	with(open('1.txt', 'r') as input_file):
		puzzle_input = input_file.read()
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	