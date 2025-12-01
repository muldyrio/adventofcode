from collections import defaultdict

def part_1(puzzle_input: str) -> int:
	connections = [tuple(d.split('-')) for d in puzzle_input.split('\n')]
	connections_dict = defaultdict(set)
	for a, b in connections:
		connections_dict[a] |= {b}
		connections_dict[b] |= {a}
	triplets = set()
	for a in connections_dict:
		for b in connections_dict[a]:
			for c in connections_dict[b]:
				if c in connections_dict[a]:
					triplets.add(tuple(sorted((a, b, c))))
	return sum(any(d[0] == 't' for d in triplet) for triplet in triplets)

def part_2(puzzle_input: str) -> int:
	connections = [tuple(d.split('-')) for d in puzzle_input.split('\n')]
	E = defaultdict(set)
	for a, b in connections:
		E[a] |= {b}
		E[b] |= {a}
	V = {c[0] for c in connections} | {c[1] for c in connections}
	V = sorted(V, key=lambda v: len(E[v]), reverse=True)
	print(V)


def main():
	with(open('23.txt', 'r') as input_file):
		puzzle_input = input_file.read()[:-1]
		
#	print(part_1(puzzle_input))
	print(part_2('''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''))

if __name__ == '__main__':
	main()
	