from collections import defaultdict

data = [line.split(",") for line in open("input.txt").readlines()]
data = [tuple(int(x) for x in line) for line in data]

def part1(data):
    edges = []
    for i, (x1, y1, z1) in enumerate(data):
        for (x2, y2, z2) in data[i+1:]:
            d = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**.5
            edges.append((d, (x1, y1, z1), (x2, y2, z2)))
    edges.sort()

    adjacency = defaultdict(set)
    for (d, a, b) in edges[:1000]:
        adjacency[a].add(b)
        adjacency[b].add(a)
    
    sets = []

    unconnected = set(data)
    while unconnected:
        n = unconnected.pop()
        visited = {n}
        to_visit = set(adjacency[n])
        while to_visit:
            m = to_visit.pop()
            visited.add(m)
            to_visit |= adjacency[m] - visited
        unconnected -= visited
        sets.append(visited)
    
    (c1, c2, c3) = sorted([len(s) for s in sets])[-3:]
    return (c1*c2*c3)

def part2(data):
    edges = []
    for i, (x1, y1, z1) in enumerate(data):
        for (x2, y2, z2) in data[i+1:]:
            d = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**.5
            edges.append((d, (x1, y1, z1), (x2, y2, z2)))
    edges.sort()

    sets = {frozenset({a}) for a in data}
    for (_, a, b) in edges:
        for s in sets:
            if a in s:
                a_set = s
            if b in s:
                b_set = s
        if b in a_set:
            continue
        sets -= {a_set, b_set}
        sets.add(frozenset(a_set | b_set))
        if len(sets) == 1:
            return a[0] * b[0]

    return

print(part1(data))
print(part2(data))