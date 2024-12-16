import numpy as np

def dijkstra(nodes: list, edges: dict, start: tuple, end: tuple) -> tuple:
	unvisited = nodes[:]
	distances = {n: np.inf for n in nodes}
	distances[start] = 0
	parent = {}
	while unvisited:
		current = min(unvisited, key=lambda x: distances[x])
		if current[0] == end:
			return (distances, current, parent)
		neighbours = (n for n in nodes if (current, n) in edges)
		for n in neighbours:
			if distances[current] + edges[(current, n)] <= distances[n]:
				if n in parent:
					parent[n].append(current)
				else:
					parent[n] = [current]
				distances[n] = distances[current] + edges[(current, n)]
		unvisited.remove(current)

def construct_graph(maze: np.array) -> tuple:
	start = tuple(np.argwhere(maze == 'S')[0])
	end = tuple(np.argwhere(maze == 'E')[0])
	maze[start] = '.'
	maze[end] = '.'
	path = [tuple(d) for d in np.argwhere(maze == '.')]
	nodes = []
	for p in path:
		neighbours = [maze[j] for j in ((p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1))]
		if neighbours.count('.') != 2 or neighbours[0] != neighbours[1]:
			nodes += [(p, d) for d in range(4)]
	
	edges = {}
	for p in nodes:
		edges[(p, (p[0], (p[1]+1) % 4))] = 1000
		edges[(p, (p[0], (p[1]-1) % 4))] = 1000
		neighbour = None
		if p[1] == 0 and maze[p[0][0]-1, p[0][1]] == '.':
			neighbour = max((n[0] for n in nodes if n[0][1] == p[0][1] and n[0][0] < p[0][0]), key=lambda x: x[0])
			dist = p[0][0] - neighbour[0]
		if p[1] == 1 and maze[p[0][0], p[0][1]+1] == '.':
			neighbour = min((n[0] for n in nodes if n[0][0] == p[0][0] and n[0][1] > p[0][1]), key=lambda x: x[1])
			dist = neighbour[1] - p[0][1]
		if p[1] == 2 and maze[p[0][0]+1, p[0][1]] == '.':
			neighbour = min((n[0] for n in nodes if n[0][1] == p[0][1] and n[0][0] > p[0][0]), key=lambda x: x[0])
			dist = neighbour[0] - p[0][0]
		if p[1] == 3 and maze[p[0][0], p[0][1]-1] == '.':
			neighbour = max((n[0] for n in nodes if n[0][0] == p[0][0] and n[0][1] < p[0][1]), key=lambda x: x[1])
			dist = p[0][1] - neighbour[1]
		if not neighbour is None:
			edges[(p, (neighbour, p[1]))] = dist
	return (nodes, edges)

def line(p: tuple, q: tuple) -> set:
	if p == q:
		return set()
	if p[0] == q[0]:
		sign = int(p[1] < q[1]) - int(p[1] > q[1])
		return {(p[0], i) for i in range(p[1], q[1]+sign, sign)}
	if p[1] == q[1]:
		sign = int(p[0] < q[0]) - int(p[0] > q[0])
		return {(i, p[1]) for i in range(p[0], q[0]+sign, sign)}

def get_paths(parent: dict, start: tuple, end: tuple) -> list:
	paths = set()
	current = [end]
	while not start in current:
		next_current = []
		for p in current:
			for q in parent[p]:
				paths |= line(p[0], q[0])
				next_current.append(q)
		current = next_current
	return paths

def part_1(puzzle_input: str) -> int:
	maze = np.array([list(d) for d in puzzle_input.split('\n')])
	start = tuple(np.argwhere(maze == 'S')[0])
	end = tuple(np.argwhere(maze == 'E')[0])
	nodes, edges = construct_graph(maze)
	distances, end, _ = dijkstra(nodes, edges, (start, 1), end)
	return distances[end]

def part_2(puzzle_input: str) -> int:
	maze = np.array([list(d) for d in puzzle_input.split('\n')])
	start = tuple(np.argwhere(maze == 'S')[0])
	end = tuple(np.argwhere(maze == 'E')[0])
	nodes, edges = construct_graph(maze)
	distances, end, parent = dijkstra(nodes, edges, (start, 1), end)
	paths = get_paths(parent, (start, 1), end)
	return len(paths)

def main():
	with(open('16.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	