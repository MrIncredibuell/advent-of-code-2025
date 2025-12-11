from functools import cache

lines = open("input.txt").read().split("\n")
data = []
for line in lines:
    source, dests = line.split(": ")
    dests = dests.split(" ")
    data.append((source, dests))


def part1(data):
    graph = {src: dest for src, dest in data}

    @cache
    def dfs(src, dest):
        if src == dest:
            return 1
        paths = 0
        for n in graph.get(src, []):
            paths += dfs(n, dest)
        return paths

    return dfs("you", "out")

def part2(data):
    graph = {src: dest for src, dest in data}

    @cache
    def dfs(src, dest):
        if src == dest:
            return 1, 0, 0, 0
        nil = 0
        fft = 0
        dac = 0
        both = 0
        for n in graph.get(src, []):
            nils, fs, ds, boths = dfs(n, dest)
            if src == "fft":
                fft += nils + fs
                both += ds + boths
            elif src == "dac":
                dac += nils + ds
                both += fs + boths
            else:
                nil += nils
                fft += fs
                dac += ds
                both += boths
            

        return (nil, fft, dac, both)

    return dfs("svr", "out")[-1]

print(part1(data))
print(part2(data))