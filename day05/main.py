ranges, ids = open("input.txt").read().split("\n\n")
ranges = [r.split("-") for r in ranges.split("\n")]
ranges = [(int(x), int(y)) for (x, y) in ranges]
ids = [int(i) for i in ids.split("\n")]

def part1(ranges, ids):
    n = 0
    for i in ids:
        for x, y in ranges:
            if x <= i <= y:
                n += 1
                break
    return n

def part2(ranges):
    to_check = set(ranges)
    found = set()
    while to_check:
        (a,b) = to_check.pop()
        to_add = None
        for (x, y) in found:
            if a <= x <= b <= y:
                found.remove((x,y))
                to_add = (a, y)
                break
            if a <= x <= y <= b:
                found.remove((x,y))
                to_add = (a, b)
                break
            if x <= a <= b <= y:
                to_add = "skip"
                break
            if x <= a <= y <= b:
                found.remove((x,y))
                to_add = (x, b) 
                break
        if to_add == "skip":
            pass
        elif to_add:
            to_check.add(to_add)
        else:
            found.add((a, b))
    
    total = 0
    for a, b in sorted(found):
        total += (b - a + 1)

    return total

print(part1(ranges, ids))
print(part2(ranges))