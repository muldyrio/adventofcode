import sys
import os

def generate_template(title: str) -> None:
	template = f'''def solution(puzzle_input: str) -> None:
	# Process input


	# Part 1


	# Part 2


def main():
	with(open('{title}.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		solution(puzzle_input)

if __name__ == '__main__':
	main()
	'''

	with open(f'{title}.py', 'w') as prog_file:
		prog_file.write(template)

def main():
	day = sys.argv[1:]
	if not day:
		files = [file for file in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), file))]
		python_files = [os.path.splitext(file)[0] for file in files if os.path.splitext(file)[1] == '.py']
		try:
			day = max(map(int, python_files)) + 1
		except ValueError:
			day = 0
	generate_template(day)

if __name__ == '__main__':
	main()