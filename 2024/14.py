import re

class Robot():
	def __init__(self, p_x: int, p_y: int, v_x: int, v_y: int):
		self.p_x = p_x
		self.p_y = p_y
		self.v_x = v_x
		self.v_y = v_y
		self.quadrant = None
	
	def __repr__(self):
		return str((self.p_x, self.p_y, self.quadrant))
	
	def update(self, w: int=101, h: int=103):
		self.p_x = (self.p_x + self.v_x) % w
		self.p_y = (self.p_y + self.v_y) % h
		self.quadrant = (self.p_x > (w // 2)) + 2 * (self.p_y > (h // 2))
		if self.p_x == w // 2 or self.p_y == h // 2:
			self.quadrant = None

def point_clustering(p: tuple, points: set) -> int:
	neighbours = {(p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1)}
	return len(neighbours.intersection(points))

def clustering(points: set) -> int:
	return sum(map(lambda x: point_clustering(x, points), points))

def print_points(points: set, w: int=101, h: int=103) -> None:
	_map = ('.' * w + '\n') * h
	for point in points:
		index = point[1] * (w+1) + point[0]
		_map = _map[:index] + '*' + _map[index+1:]
	print(_map)

def part_1(puzzle_input: str) -> int:
	pattern = r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)'
	robots = []
	for robot_pars in re.findall(pattern, puzzle_input):
		robots.append(Robot(*map(int, robot_pars)))
	for _ in range(100):
		for robot in robots:
			robot.update()
	res = 1
	for q in range(4):
		res *= len([robot for robot in robots if robot.quadrant == q])
	return res

def part_2(puzzle_input: str) -> int:
	pattern = r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)'
	robots = []
	for robot_pars in re.findall(pattern, puzzle_input):
		robots.append(Robot(*map(int, robot_pars)))
	max_clustering = 0
	i = 0
	while True:
		points = {(r.p_x, r.p_y) for r in robots}
		c = clustering(points)
		if c > max_clustering:
			i_max = i
			max_clustering = c
			print(i_max)
			print_points(points)
		for robot in robots:
			robot.update()
		i += 1

def main():
	with(open('14.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	