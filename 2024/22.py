from collections import defaultdict

def mix(x: int, y: int) -> int:
	return x ^ y

def prune(x: int) -> int:
	return x & 16777215

def next_secret(x: int) -> int:
	x = prune(mix(x, x << 6))
	x = prune(mix(x, x >> 5))
	x = prune(mix(x, x << 11))
	return x	

def secret(seed: int, n_iter: int) -> int:
	for _ in range(n_iter):
		seed = next_secret(seed)
	return seed

def part_1(puzzle_input: str) -> int:
	seeds = (int(d) for d in puzzle_input.split('\n'))
	return sum(secret(seed, 2000) for seed in seeds)

def part_2(puzzle_input: str) -> int:
	seeds = (int(d) for d in puzzle_input.split('\n'))
	prices = []
	for i, seed in enumerate(seeds):
		prices.append((seed, ))
		for _ in range(2000):
			seed = next_secret(seed)
			prices[i] += (seed % 10, )
	diffs = [tuple(d[i+1]-d[i] for i in range(2000)) for d in prices]
	values = defaultdict(int)
	for i, price in enumerate(prices):
		seen = set()
		for j in range(1997):
			seq = diffs[i][j:j+4]
			val = price[j+4]
			if not seq in seen:
				seen.add(seq)
				values[seq] += val
	return max(values.values())

def main():
	with(open('22.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
	#print(part_1(puzzle_input))
	print(part_2(puzzle_input))

if __name__ == '__main__':
	main()
	