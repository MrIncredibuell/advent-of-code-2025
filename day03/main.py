from functools import cache

data = open("input.txt").read().split("\n")

def part1(data):
    total = 0
    for line in data:
        best = 0
        for i, c1 in enumerate(line[:-1]):
            for c2 in line[i+1:]:
                if (x := int(c1 + c2)) > best:
                    best = x
        total += best
    return total

@cache
def sub(line, n):
    if n == 1:
        return max([int(c) for c in line])
    if len(line) == n:
        return int("".join(line))
    best = 0
    for i, c in enumerate(line[:-n + 1]):
        x = int(c + str(sub(line[i+1:], n-1)))
        best = max(best, x)
    return best

def part2(data):
    total = 0
    for line in data:
        x = sub(line, 12)
        total += x
    return total

print(part1(data))
print(part2(data))