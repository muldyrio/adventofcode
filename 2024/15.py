import numpy as np

def try_move(_map: np.array, index: np.array, _dir: np.array) -> np.array:
	i = 0
	while True:
		i += 1
		check = index + i * _dir
		if _map[*check] == '#':
			return index
		if _map[*check] == '.':
			break
	
	for _ in range(i, 0, -1):
		_map[*check] = _map[*(check-_dir)]
		check = check-_dir
	_map[*index] = '.'
	return index+_dir

def embiggen(_map: str):
	return _map.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')

def to_be_moved(_map: np.array, index: np.array, _dir: np.array) -> dict:
	x_range = (index[1], )
	indices = {0: x_range}
	y = index[0]
	i = 0
	dy = _dir[0]
	while True:
		if all(s == '.' for s in _map[y+dy, indices[i]]):
			return indices
		if any(s == '#' for s in _map[y+dy, indices[i]]):
			return None
		i += 1
		y += dy
		x_range = set()
		for x in indices[i-1]:
			if _map[y, x] == ']':
				x_range.add(x)
				x_range.add(x-1)
			if _map[y, x] == '[':
				x_range.add(x)
				x_range.add(x+1)
		indices[i] = tuple(x_range)

def try_move_2(_map: np.array, index: np.array, _dir: np.array) -> np.array:
	move_dict = to_be_moved(_map, index, _dir)
	if move_dict is None:
		return index
	
	for dy in sorted(move_dict, reverse=True):
		y0 = index[0] + dy * _dir[0]
		y1 = index[0] + (dy + 1) * _dir[0]
		for x in move_dict[dy]:
			_map[y0, x], _map[y1, x] = _map[y1, x], _map[y0, x]
	
	return index + _dir

def print_map(_map: np.array) -> None:
	print('\n'.join(''.join(d) for d in _map))

def part_1(puzzle_input: str) -> int:
	_map, moves = puzzle_input.split('\n\n')
	moves = moves.replace('\n', '')
	dirs_dict = {
		'<': np.array([ 0, -1]),
		'>': np.array([ 0,  1]),
		'^': np.array([-1,  0]),
		'v': np.array([ 1,  0])
	}
	_map = np.array([list(d) for d in _map.split('\n')])
	index = np.argwhere(_map == '@')[0]
	for move in moves:
		_dir = dirs_dict[move]
		index = try_move(_map, index, _dir)
	
	res = 0
	for box in np.argwhere(_map == 'O'):
		res += 100 * box[0] + box[1]
	return res

def part_2(puzzle_input: str) -> int:
	_map, moves = puzzle_input.split('\n\n')
	moves = moves.replace('\n', '')
	dirs_dict = {
		'<': np.array([ 0, -1]),
		'>': np.array([ 0,  1]),
		'^': np.array([-1,  0]),
		'v': np.array([ 1,  0])
	}
	_map = embiggen(_map)
	_map = np.array([list(d) for d in _map.split('\n')])
	index = np.argwhere(_map == '@')[0]
	for move in moves:
		_dir = dirs_dict[move]
		if move == '<' or move == '>':
			index = try_move(_map, index, _dir)
		else:
			index = try_move_2(_map, index, _dir)
	
	res = 0
	for box in np.argwhere(_map == '['):
		res += 100 * box[0] + box[1]
	return res

def main():
	with(open('15.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	