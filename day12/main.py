from functools import cache

segments = open("input.txt").read().split("\n\n")
shapes = []
regions = []
for shape in segments[:-1]:
    shape_set = set()
    for y, line in enumerate(shape.split("\n")[1:]):
        for x, c in enumerate(line):
            if c == "#":
                shape_set.add((x, y))
    shapes.append(frozenset(shape_set))
        
for region in segments[-1].split("\n"):
    size, quantities = region.split(": ")
    size = tuple(int(x) for x in size.split("x"))
    quantities = [int(x) for x in quantities.split(" ")]
    regions.append((size, quantities))


def part1(shapes, regions):
    total = 0
    for size, quantities in regions:
        a = 0
        for i, q in enumerate(quantities):
            a += len(shapes[i]) * q
        if a < size[0] * size[1]:
            total += 1

    return total



print(part1(shapes, regions))