data = [x.split("-") for x in open("input.txt").read().split(",")]
data = [(int(a), int(b)) for a, b in data]

def part1(data):
    total = 0
    for start, end in data:
        i = start
        while i <= end:
            digits = str(i)
            l = len(digits)
            m = l // 2
            if digits[:m] == digits[m:]:
                total += i
            i += 1

    return total

def part2(data):
    total = 0
    for start, end in data:
        i = start
        while i <= end:
            digits = str(i)
            l = len(digits)
            for j in range(1, l):
                if int(digits[:j] * (l // j)) == i:
                    # print(i)
                    total += i
                    break

            i += 1

    return total

print(part1(data))
print(part2(data))