def get_disk_table(disk_str: str) -> tuple:
	progs = []
	empty = []
	index = 0
	for i, n in enumerate(disk_str):
		if i % 2 == 0:
			progs.append([index, int(n)])
		else:
			empty.append([index, int(n)])
		index += int(n)
	return (progs, empty)

def checksum(disk: list) -> int:
	res = 0
	for i, n in enumerate(disk):
		if n is not None:
			res += i * n
	return res

def fragment_disk(disk: list, empty_indices: list) -> list:
	progs = [i for i in disk if i is not None]
	for i, index in enumerate(empty_indices):
		disk[index] = progs[-(i+1)]
	disk[len(progs):] = (len(disk)-len(progs)) * [None]
	return disk

def cleanup(empty: list) -> list:
	cleaned = sorted([e for e in empty if e[1] != 0])
	while True:
		for i, e in enumerate(cleaned[:-1]):
			if sum(e) == cleaned[i+1][0]:
				e[1] += cleaned[i+1][1]
				del cleaned[i+1]
				break
		else:
			break
	return cleaned

def part_1(puzzle_input: str) -> str:
	disk = []
	empty_indices = []
	for i, n in enumerate(puzzle_input):
		if i % 2 == 0:
			disk = disk + int(n) * [i // 2]
		else:
			empty_indices += list(range(len(disk), len(disk)+int(n)))
			disk = disk + int(n) * [None]

	fragmented = fragment_disk(disk, empty_indices)
	return checksum(fragmented)

def part_2(puzzle_input: str) -> str:
	disk = []
	for i, n in enumerate(puzzle_input):
		if i % 2 == 0:
			disk = disk + int(n) * [i // 2]
		else:
			disk = disk + int(n) * [None]

	progs, empty = get_disk_table(puzzle_input)
	n_progs = len(progs)
	for i, prog in enumerate(progs[::-1]):
		_id = n_progs - i - 1
		for space in empty:
			if space[1] >= prog[1] and space[0] < prog[0]:
				disk[space[0]:space[0]+prog[1]] = prog[1] * [_id]
				disk[prog[0]:sum(prog)] = prog[1] * [None]
				space[0] += prog[1]
				space[1] -= prog[1]
				empty.append(prog)
				break
		empty = cleanup(empty)
		
	return checksum(disk)

def main():
	with(open('9.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))


if __name__ == '__main__':
	main()