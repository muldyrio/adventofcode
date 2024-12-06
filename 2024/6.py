import numpy as np


class Guard:
	def __init__(self, _map: np.array, pos: tuple, _dir: np.array):
		self.pos = np.array(pos)
		self._map = _map
		self.visited = {pos}
		self._dir = _dir
		self.in_map = True

	def __bool__(self):
		return self.in_map
	
	def __repr__(self):
		return str(self.pos)

	def move(self):
		if not self.in_map:
			pass

		next_pos = self.pos + self._dir
		if (next_pos[0] in {-1, self._map.shape[0]}) or (next_pos[1] in {-1, self._map.shape[1]}):
			self.in_map = False
		elif self._map[*next_pos] == '#':
			self._dir = np.array([self._dir[1], -self._dir[0]])
			self.move()
		else:
			self.pos = next_pos
			self.visited.add(tuple(next_pos))


def pos_dir_hash(pos: np.array, _dir: np.array) -> tuple:
	dir_hash = {d:i for i, d in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)])}[(_dir[0], _dir[1])]
	return (pos[0], pos[1], dir_hash)

def does_loop(guard: Guard) -> bool:
	visited_dir = set()
	while guard:
		next_pos_dir = pos_dir_hash(guard.pos, guard._dir)
		if next_pos_dir in visited_dir:
			return True
		guard.move()

		visited_dir.add(next_pos_dir)
	return False

def part_1(puzzle_input: str) -> str:
	rows = [list(s) for s in puzzle_input[:-1].split('\n')]
	_map = np.array(rows)
	pos = tuple(d[0] for d in np.where(_map == '^'))
	_dir = np.array([-1, 0])
	G = Guard(_map, pos, _dir)
	while G:
		G.move()
	
	return len(G.visited)

def part_2(puzzle_input: str) -> str:
	rows = [list(s) for s in puzzle_input[:-1].split('\n')]
	_map = np.array(rows)
	pos = tuple(d[0] for d in np.where(_map == '^'))
	_dir = np.array([-1, 0])
	res = 0
	for i in range(_map.shape[0]):
		for j in range(_map.shape[1]):
			if _map[i, j] == '.':
				_map = np.array(rows)
				_map[i, j] = '#'
				G = Guard(_map, pos, _dir)
				res += does_loop(G)
	return res

def main():
	with(open('6.txt', 'r') as input_file):
		puzzle_input = input_file.read()
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	