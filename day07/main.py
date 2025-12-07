from functools import cache

data = open("input.txt").read().split()

def part1(data):
    count = 0
    xs = {}
    for line in data[1:]:
        for x, c in enumerate(line):
            if c == '^' and x in xs:
                xs.remove(x)
                xs |= {x+1, x-1}
                count += 1

    return count

def part2(data):
    @cache
    def sub(y, x):
        if y == len(data) - 1:
            return 1
        if data[y][x] == "^":
            return sub(y + 1, x - 1) + sub(y + 1, x + 1)
        return sub(y + 1, x)
    
    x = data[0].index("S")
        
    return sub(1, x)

print(part1(data))
print(part2(data))