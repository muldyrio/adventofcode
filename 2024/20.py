import numpy as np
from itertools import permutations

def get_dists(track: np.array, start: tuple, end: tuple) -> dict:
	track_local = track[:,:]
	dists = {}
	index = start
	dist = 0
	while index != end:
		track[index] = '#'
		dists[index] = dist
		y, x = index
		offsets = ((y-1, x), (y+1, x), (y, x-1), (y, x+1))
		neighbours = [track[o] for o in offsets]
		index = offsets[neighbours.index('.')]
		dist += 1
	dists[end] = dist
	return dists

def cheat_locations(track: np.array) -> list:
	h, w = track.shape
	inner_track = track[1:h-1, 1:w-1]
	inner_walls = np.argwhere(inner_track == '#')
	inner_walls = (d + np.array([1, 1]) for d in inner_walls)
	locations = []
	for wall in inner_walls:
		neighbours = np.array([wall + d for d in np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])])
		good_neighbours = []
		for n in neighbours:
			if track[*n] == '.':
				good_neighbours.append(tuple(n))
		if len(good_neighbours) >= 2:
			locations.append((tuple(wall), good_neighbours))
	return locations

def cheat_values(cheat: tuple, dists_start: dict, dists_end: dict) -> list:
	wall, paths = cheat
	A = min(paths, key=lambda x: dists_start[x])
	paths.remove(A)
	values = []
	dist_A = dists_start[A] + dists_end[A]
	for B in paths:
		dist_cheat = dists_start[A] + dists_end[B] + 2
		if dist_cheat < dist_A:
			values.append(dist_A - dist_cheat)
	return values

def part_1(puzzle_input: str) -> int:
	track = np.array([list(d) for d in puzzle_input.split('\n')])
	start = tuple(np.argwhere(track == 'S')[0])
	end = tuple(np.argwhere(track == 'E')[0])
	track[*start] = '.'
	track[*end] = '.'
	dists_start = get_dists(np.copy(track), start, end)
	dists_end = {d: dists_start[end]-dists_start[d] for d in dists_start}
	cheat_saves = []
	for cheat in cheat_locations(track):
		cheat_saves += cheat_values(cheat, dists_start, dists_end)
	return sum(d >= 100 for d in cheat_saves)
	

def part_2(puzzle_input: str) -> int:
	track = np.array([list(d) for d in puzzle_input.split('\n')])
	start = tuple(np.argwhere(track == 'S')[0])
	end = tuple(np.argwhere(track == 'E')[0])
	track[*start] = '.'
	track[*end] = '.'
	dists_start = get_dists(np.copy(track), start, end)
	dists_end = {d: dists_start[end]-dists_start[d] for d in dists_start}


def main():
	with(open('20.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	print(part_1(puzzle_input))
	print(part_2('''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''))

if __name__ == '__main__':
	main()
	