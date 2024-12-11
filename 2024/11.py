def read_input():
    with open("2024/input/11.txt") as f:
        return f.read().strip()


inp = list(map(int, read_input().split()))
# inp = [125, 17]
n = len(inp)


def part1():
    res = None
    for _ in range(25):
        curr = res[:] if res else inp[:]
        res = []
        for i in range(len(curr)):
            if curr[i] == 0:
                res.append(1)
            elif len(str(curr[i])) % 2 == 0:
                l = len(str(curr[i]))
                res.append(int(str(curr[i])[: l // 2]))
                res.append(int(str(curr[i])[l // 2 :]))
            else:
                res.append(curr[i] * 2024)

    return len(res)


dp = {}


def dfs(num, iteration):
    if (num, iteration) in dp:
        return dp[(num, iteration)]

    if iteration == 0:
        return 1

    res = 0
    l = len(str(num))
    if num == 0:
        res = dfs(1, iteration - 1)
    elif l % 2 == 0:
        res = dfs(int(str(num)[: l // 2]), iteration - 1) + dfs(
            int(str(num)[l // 2 :]), iteration - 1
        )
    else:
        res = dfs(num * 2024, iteration - 1)

    dp[(num, iteration)] = res
    return res


def part2():
    res = 0
    for i in inp:
        res += dfs(i, 75)
    return res


print(part1())
print(part2())
