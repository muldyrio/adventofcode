import numpy as np
from collections.abc import Iterable

def construct_maze(walls: Iterable[tuple], h: int, w: int, n_walls: int) -> np.array:
	if type(walls) == list:
		walls = (w for w in walls)
	maze = np.zeros((h+3, w+3), bool)
	maze[1:h+2, 1:w+2] = True
	for _ in range(n_walls):
		wall = next(walls)
		maze[wall[1]+1, wall[0]+1] = False
	return maze

def construct_graph(maze: np.array) -> tuple:
	h, w = maze.shape
	nodes = []
	edges = {}
	for i in range(1, h-1):
		for j in range(1, w-1):
			if maze[i, j]:
				nodes.append((i, j))
				for n in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
					if maze[n]:
						edges[((i, j), n)] = 1
	return (nodes, edges)

def dijkstra(nodes: list, edges: dict, start: tuple, end: tuple) -> tuple:
	unvisited = nodes[:]
	distances = {n: np.inf for n in nodes}
	distances[start] = 0
	parent = {}
	while unvisited:
		current = min(unvisited, key=lambda x: distances[x])
		if current == end:
			return (distances, parent)
		neighbours = (n for n in nodes if (current, n) in edges)
		for n in neighbours:
			if distances[current] + edges[(current, n)] <= distances[n]:
				if n in parent:
					parent[n].append(current)
				else:
					parent[n] = [current]
				distances[n] = distances[current] + edges[(current, n)]
		unvisited.remove(current)

def get_component(i: tuple, maze: np.array) -> set:
	component = {i}
	while True:
		border = set()
		for j in component:
			y, x = j
			border |= {(y+1, x), (y-1, x), (y, x+1), (y, x-1)} - component
		same_component = {n for n in border if maze[n]}
		if not same_component:
			return component
		component |= same_component

def part_1(puzzle_input: str) -> int:
	byte_positions = (tuple(map(int, d.split(','))) for d in puzzle_input.split('\n'))
	h, w = 70, 70
	maze = construct_maze(byte_positions, h, w, 1024)
	nodes, edges = construct_graph(maze)
	costs, _ = dijkstra(nodes, edges, (1, 1), (h+1, w+1))
	return costs[(h+1, w+1)]

def part_2(puzzle_input: str) -> tuple:
	byte_positions = [tuple(map(int, d.split(','))) for d in puzzle_input.split('\n')]
	h, w = 70, 70
	upper = len(byte_positions)
	lower = 0
	while True:
		if lower == upper-1:
			return byte_positions[lower]
		
		mid = (lower + upper) // 2
		maze = construct_maze(byte_positions, h, w, mid)
		end_component = get_component((h+1, w+1), maze)
		if (1, 1) in end_component:
			lower = mid
		else:
			upper = mid

def main():
	with(open('18.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	