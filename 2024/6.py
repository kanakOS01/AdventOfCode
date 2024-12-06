def read_input():
    with open("2024/input/6.txt") as f:
        return f.read().strip()


inp = read_input().splitlines()
grid = [list(row) for row in inp]
n = 130


def part1():
    s = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "^":
                s = (i, j)
                break
        if s:
            break

    visited = set()
    dir = (-1, 0)
    i, j = s
    while 0 <= i < n and 0 <= j < n:
        visited.add((i, j))
        di, dj = dir
        ni, nj = i + di, j + dj
        if not (0 <= ni < n and 0 <= nj < n):
            break
        if grid[ni][nj] == "#":
            dir = (dj, -di)
        else:
            i = ni
            j = nj

    return len(visited)


def check_cycle(s, grid):
    visited = set()
    dir = (-1, 0)
    i, j = s
    while 0 <= i < n and 0 <= j < n:
        if (i, j, dir) in visited:
            return True
        visited.add((i, j, dir))
        di, dj = dir
        ni, nj = i + di, j + dj
        if not (0 <= ni < n and 0 <= nj < n):
            break
        if grid[ni][nj] == "#":
            dir = (dj, -di)
        else:
            i = ni
            j = nj
    return False


def part2():
    s = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "^":
                s = (i, j)
                break
        if s:
            break

    res = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == ".":
                grid[i][j] = "#"
                if check_cycle(s, grid):
                    res += 1
                grid[i][j] = "."
    return res


print(part1())
print(part2())
