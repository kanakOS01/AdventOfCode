from collections import Counter


def read_input():
    with open("2024/input/1.txt") as f:
        return f.read().strip()


inp = read_input()
l1, l2 = [], []
for i in inp.split("\n"):
    locs = i.split()
    l1.append(int(locs[0]))
    l2.append(int(locs[1]))


def part1():
    l1.sort()
    l2.sort()
    res = 0
    for i in range(1000):
        res += abs(l1[i] - l2[i])
    return res


def part2():
    cnt = Counter(l2)
    res = 0
    for i in l1:
        res += cnt[i] * i
    return res


print(part1())
print(part2())