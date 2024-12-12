from collections import defaultdict


def read_input():
    with open("2024/input/12.txt") as f:
        return f.read().strip()
    
inp = read_input().splitlines()
n = len(inp)
dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
grid = [['*'] * (n+2) for _ in range(n+2)]
for i in range(1, n+1):
    for j in range(1, n+1):
        grid[i][j] = inp[i-1][j-1]


def dfs(i, j,  ap, vis):
    if (i, j) in vis:
        return

    vis.add((i, j))
    ap[0] += 1
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if grid[i][j] != grid[ni][nj]:
            ap[1] += 1
    
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if grid[i][j] == grid[ni][nj]:
            dfs(ni, nj, ap, vis)


def part1():    
    res = 0
    vis = set()

    for i in range(1, n+1):
        for j in range(1, n+1):
            ap = [0, 0]
            dfs(i, j, ap, vis)
            res += ap[0] * ap[1]
    
    return res
            

def part2():
    pass


print(part1())
print(part2())