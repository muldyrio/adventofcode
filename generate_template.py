import sys

def generate_template(title: str) -> None:
	template = f'''def part_1(puzzle_input: str) -> str:
	pass

def part_2(puzzle_input: str) -> str:
	pass

def main():
	with(open('{title}.txt', 'r') as input_file):
		puzzle_input = input_file.read()
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	'''

	with open(f'{title}.py', 'w') as prog_file:
		prog_file.write(template)

def main():
	day = sys.argv[1]
	generate_template(day)

if __name__ == '__main__':
	main()