print(sum([len(set(g)-set("\n")) for g in open("data/day6.txt").read().split("\n\n")]), sum([len(g[0].intersection(*g[1:])) for g in [list(map(set,g.splitlines())) for g in open("data/day6.txt").read().split("\n\n")]]))