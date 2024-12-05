def dict_from_pairs(pairs_iterable) -> dict:
	output = {}
	for pair in pairs_iterable:
		if pair[0] in output:
			output[pair[0]].add(pair[1])
		else:
			output[pair[0]] = {pair[1]}
	return output

def get_min(entries: list, rules: dict) -> str:
	current_min = entries[0]
	for entry in entries[1:]:
		if entry in rules and current_min in rules[entry]:
			current_min = entry
	return current_min

def sort(update: list, rules: dict) -> list:
	if len(update) == 1:
		return update
	min_entry = get_min(update, rules)
	min_index = update.index(min_entry)
	return [min_entry] + sort(update[:min_index] + update[min_index+1:], rules)

def part_1(puzzle_input: str) -> str:
	rules_raw, updates_raw = puzzle_input[:-1].split('\n\n')
	rules = dict_from_pairs(r.split('|') for r in rules_raw.split('\n'))
	updates = (u.split(',') for u in updates_raw.split('\n'))
	
	result = 0	
	for update in updates:
		sorted_update = sort(update, rules)
		if update == sorted_update:
			result += int(update[len(update) // 2])
	return result

def part_2(puzzle_input: str) -> str:
	rules_raw, updates_raw = puzzle_input[:-1].split('\n\n')
	rules = dict_from_pairs(r.split('|') for r in rules_raw.split('\n'))
	updates = (u.split(',') for u in updates_raw.split('\n'))
	
	result = 0	
	for update in updates:
		sorted_update = sort(update, rules)
		if update != sorted_update:
			result += int(sorted_update[len(update) // 2])
	return result

def main():
	with(open('5.txt', 'r') as input_file):
		puzzle_input = input_file.read()
	
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	