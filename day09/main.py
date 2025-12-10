from collections import defaultdict

rows = open("input.txt").read().split("\n")
data = []
for row in rows:
    x, y = row.split(",")
    data.append((int(x), int(y)))

def part1(data):
    best = 0
    for i, (x1, y1) in enumerate(data):
        for (x2, y2) in data[i+1:]:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            best = max(best, area)
    return best

def is_valid2(p1, p2, xlines):
    minx, maxx = sorted([p1[0], p2[0]])
    miny, maxy = sorted([p1[1], p2[1]])

    for y in range(miny, maxy + 1):
        xs = xlines[y]
        if not xs:
            return False
        if minx < xs[0][0]:
            return False
        winding = 0
        for (x, w) in xlines[y]:
            winding += w
            if (minx <= x < maxx) and (winding == 0):
                return False
            
    return True

def part2(data):
    x1, y1 = data[0]
    minx, miny = x1, y1
    maxx, maxy = x1, y1
    ylines = defaultdict(dict)
    xlines = defaultdict(list)
    for x2, y2 in data[1:] + [(x1, y1)]:
        minx = min(minx, x2)
        maxx = max(maxx, x2) 
        miny = min(miny, y2)
        maxy = max(maxy, y2)
        if x1 == x2:
            if y1 < y2:
                for i in range(y1, y2 + 1):
                    ylines[x1][i] = 1
                    xlines[i].append((x1, 1))
            else:
                for i in range(y2, y1 + 1):
                    ylines[x1][i] = -1
                    xlines[i].append((x1, -1))
            
        x1, y1 = x2, y2

    for k, v in xlines.items():
        xlines[k] = sorted(v)
    
    areas = []
    for i, (x1, y1) in enumerate(data):
        for (x2, y2) in data[i+1:]:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            areas.append((area, (x1, y1), (x2, y2)))

    for a, p1, p2 in sorted(areas, reverse=True):
        if is_valid2(p1, p2, xlines):
            return a

    return

print(part1(data))
print(part2(data))