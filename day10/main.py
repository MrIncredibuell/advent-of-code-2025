from scipy.optimize import milp, LinearConstraint

data = []
lines = open("input.txt").read().split("\n")
for line in lines:
    lights, *buttons, joltage = line.split(" ")
    parsed = []
    for b in buttons:
        parsed.append(tuple(int(x) for x in b[1:-1].split(",")))
    joltage = tuple(int(x) for x in joltage[1:-1].split(","))
    data.append((tuple(c for c in lights[1:-1]), parsed, joltage))

def toggle(lights, button):
    lights = [l for l in lights]
    for i in button:
        if lights[i] == "#":
            lights[i] = "."
        else:
            lights[i] = "#"
    return tuple(lights)

    
def bfs(lights, buttons):
    distances = {}
    to_visit = [(tuple(["."] * len(lights)), 0)]
    while to_visit:
        l, d = to_visit.pop(0)
        if l in distances:
            continue
        distances[l] = d
        if l == lights:
            return d
        for b in buttons:
            n = toggle(l, b)
            if n not in distances:
                to_visit.append((n, d + 1))

def part1(data):
    total = 0
    for lights, buttons, _ in data:
        total += bfs(lights, buttons)
                
    return total

def inc(joltage, button):
    joltage = list(joltage)
    for i in button:
        joltage[i] += 1
    return tuple(joltage)

def part2(data):
    total = 0
    for _, buttons, joltage in data:
        obj = [1] * len(buttons)
        A = []
        for i in range(len(joltage)):
            A.append([(1 if i in b else 0) for b in buttons])

        constraints = LinearConstraint(A=A, lb=joltage, ub=joltage)
        result = milp(c=obj, constraints=constraints, integrality=[1]*len(buttons))
        total += int(sum(result.x))
                
    return total


print(part1(data))
print(part2(data))