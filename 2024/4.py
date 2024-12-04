def read_input():
    with open("2024/input/4.txt") as f:
        return f.read().strip()


inp = read_input().splitlines()
w = ["XMAS", "SAMX"]
w2 = ["MAS", "SAM"]
n = 140


def r():
    cnt = 0
    for line in inp:
        for i in range(n):
            if i < n - 3 and line[i : i + 4] in w:
                cnt += 1
    return cnt


def c():
    cnt = 0
    for i in range(n):
        for j in range(n):
            s = (
                inp[i][j] + inp[i + 1][j] + inp[i + 2][j] + inp[i + 3][j]
                if i < n - 3
                else ""
            )
            if s in w:
                cnt += 1
    return cnt


def d():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i < n - 3 and j < n - 3:
                s = (
                    inp[i][j]
                    + inp[i + 1][j + 1]
                    + inp[i + 2][j + 2]
                    + inp[i + 3][j + 3]
                )
                if s in w:
                    cnt += 1
            if i < n - 3 and j > 2:
                s = (
                    inp[i][j]
                    + inp[i + 1][j - 1]
                    + inp[i + 2][j - 2]
                    + inp[i + 3][j - 3]
                )
                if s in w:
                    cnt += 1
    return cnt


def part1():
    return r() + c() + d()


def part2():
    res = 0
    for i in range(n):
        for j in range(n):
            d1, d2 = False, False
            if i < n - 2 and j < n - 2:
                s = inp[i][j] + inp[i + 1][j + 1] + inp[i + 2][j + 2]
                if s in w2:
                    d1 = True

            if d1:
                k = j + 2
                if i < n - 2 and k > 1 and k < n:
                    s = inp[i][k] + inp[i + 1][k - 1] + inp[i + 2][k - 2]
                    if s in w2:
                        d2 = True

            if d1 and d2:
                res += 1
    return res


print(part1())
print(part2())
