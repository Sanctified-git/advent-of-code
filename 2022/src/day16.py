"""https://adventofcode.com/2022/day/16"""
from utils.io import get_input
from utils.timer import Timer
from re import findall
from collections import defaultdict
from functools import partial
from itertools import product, combinations
from math import inf as INFINITY

TIME = 30
START = "AA"


def parse_input(input: list) -> tuple[dict, dict, dict]:
    valves: dict = {
        (matches := [m for m in findall(r"([A-Z]{2})", line)])[0]: matches[1:]
        for line in input
    }
    flow_rates: dict = {
        v: int(fr) for line in input for v, fr in findall(r"([A-Z]{2}).*=(\d+)", line)
    }
    return valves, flow_rates


def floyd_warshall(graph):
	distance = defaultdict(lambda: defaultdict(lambda: INFINITY))

	for a, bs in graph.items():
		distance[a][a] = 0
		for b in bs:
			distance[a][b] = 1
			distance[b][b] = 0

	for a, b, c in product(graph, graph, graph):
		bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]
		if ba + ac < bc:
			distance[b][c] = ba + ac
	return distance


def score(flow_rates, path):
    result = 0
    for valve, time_left in path.items():
        result += flow_rates[valve] * time_left
    return result


def solutions(distance, flow_rates, valves, time=TIME, cur=START, chosen={}):
	for nxt in valves:
		new_time = time - distance[cur][nxt] - 1
		if new_time < 2:
			continue

		new_chosen = chosen | {nxt: new_time}
		yield from solutions(distance, flow_rates, valves - {nxt}, new_time, nxt, new_chosen)
	yield chosen
    

if __name__ == "__main__":
    t = Timer()
    t.start()
    print("Parsing input")
    valves, flow_rates = parse_input(get_input(__file__))

    t.step()
    ### PART ONE ###
    good     = frozenset(filter(flow_rates.get, valves))
    distance = floyd_warshall(valves)
    score    = partial(score, flow_rates)

    best     = max(map(score, solutions(distance, valves, good)))
    print(f"{best} pressure can be relieved at most in {TIME} minutes")
    t.step()

    ### PART TWO ###
    maxscore = defaultdict(int)

    # for solution in solutions(distance, flow_rates, good, TIME-4):
    #     if (s:= score(solution)) > maxscore[(k := frozenset(solution))]:
    #         maxscore[k] = s

    for solution in solutions(distance, flow_rates, good, TIME-4):
        k = frozenset(solution)
        s = score(solution)

        if s > maxscore[k]:
            maxscore[k] = s

    best = max(sa + sb for (a, sa), (b, sb) in combinations(maxscore.items(), 2) if not a & b)
    print(f"{best} pressure can be relieved at most with the help of an elephant")
    t.stop()
