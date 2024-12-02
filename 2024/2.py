def read_input():
    with open("2024/input/2.txt") as f:
        return f.read().strip()


inp = read_input().splitlines()
l = []
for line in inp:
    l.append(list(map(int, line.split(" "))))


def inc(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def dec(l):
    return all(l[i] >= l[i + 1] for i in range(len(l) - 1))


def diff(l):
    return all(1 <= abs(l[i] - l[i - 1]) <= 3 for i in range(1, len(l)))


def part1():
    cnt = 0
    for arr in l:
        if (inc(arr) or dec(arr)) and diff(arr):
            cnt += 1
    return cnt


def part2():
    cnt = 0
    for arr in l:
        if (inc(arr) or dec(arr)) and diff(arr):
            cnt += 1
        else:
            for i in range(len(arr)):
                temp = arr[:i] + arr[i + 1 :]
                if (inc(temp) or dec(temp)) and diff(temp):
                    cnt += 1
                    break
    return cnt


print(part1())
print(part2())
