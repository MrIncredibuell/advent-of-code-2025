lines = open("input.txt").read().split()
data = {}
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        data[(j, i)] = c

def part1(data):
    count = 0
    for (x,y), c in data.items():
        if c != "@":
            continue
        n = 0
        for (dx, dy) in [
            (1, 1),
            (0, 1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]:
          if data.get((x + dx, y + dy), ".") == "@":
              n += 1
        if n < 4:
            count += 1 
    return count

def part2(data):
    running = True
    count = 0
    while running:
        running = False
        new_data = {}
        for (x,y), c in data.items():
            if c != "@":
                continue
            n = 0
            for (dx, dy) in [
                (1, 1),
                (0, 1),
                (-1, 0),
                (1, 0),
                (-1, 1),
                (1, -1),
                (0, -1),
                (-1, -1),
            ]:
                if data.get((x + dx, y + dy), ".") == "@":
                    n += 1
            if n < 4:
                count += 1
                running = True
            else:
                new_data[(x,y)] = c
        data = new_data

    return count

# print(part1(data))
print(part2(data))