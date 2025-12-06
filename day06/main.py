data = open("input.txt").read().split("\n")


def part1(data):
    data = [[x for x in row.split(" ") if x != ''] for row in data]
    total = 0
    for i in range(len(data[0])):
        op = data[-1][i]
        if op == '*':
            n  = 1
        else:
            n = 0
        for j in range(len(data) - 1):
            if op == '+':
                n += int(data[j][i])
            else:
                n *= int(data[j][i])
        total+= n
    return total

def part2(data):
    total = 0
    ns = []
    for i in range(len(data[0]) - 1, -1, -1):
        s = ''
        for j in range(len(data) - 1):
            if (c := data[j][i]) != ' ':
                s += c
        if s != '':
            ns.append(int(s))
        if data[-1][i] == '+':
            total += sum(ns)
            ns = []
        elif data[-1][i] == '*':
            product = 1
            for n in ns:
                product *= n
            total += product
            ns = []
    return total

print(part1(data))
print(part2(data))