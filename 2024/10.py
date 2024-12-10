def read_input():
    with open("2024/input/10.txt") as f:
        return f.read().strip()


inp = read_input().splitlines()
grid = [list(map(int, i)) for i in inp]
n = len(grid)
dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def dfs(i, j, visited):
    if grid[i][j] == 9 and (i, j) not in visited:
        visited.add((i, j))
        return 1

    res = 0
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] - grid[i][j] == 1:
            res += dfs(ni, nj, visited)

    return res


def part1():
    res = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                res += dfs(i, j, set())

    return res


def dfs2(i, j):
    if grid[i][j] == 9 and (i, j):
        return 1

    res = 0
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] - grid[i][j] == 1:
            res += dfs2(ni, nj)

    return res


def part2():
    res = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                res += dfs2(i, j)
    return res


print(part1())
print(part2())
