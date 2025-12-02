data = open("input.txt").readlines()

def part1(data):
    x = 50
    zeroes = 0
    for l in data:
        direction  = l[0]
        magnitude = int(l[1:])
        if direction == "L":
            x = (x - magnitude) % 100
        else:
            x = (x + magnitude) % 100
        if x == 0:
            zeroes += 1
    return zeroes

def part2(data):
    x = 50
    zeroes = 0
    for l in data:
        direction  = l[0]
        magnitude = int(l[1:])
        while magnitude >= 100:
            magnitude -= 100
            if magnitude != 0:
                zeroes += 1

        old_x = x
            
        if direction == "L":
            x = (x - magnitude)
        else:
            x = (x + magnitude)

        if x % 100 != x:
            if old_x != 0:
                zeroes += 1
            x = x % 100
        elif x == 0:
            zeroes += 1
            
    return zeroes

print(part1(data))
print(part2(data))