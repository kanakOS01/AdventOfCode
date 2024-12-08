from collections import defaultdict


def read_input():
    with open("2024/input/8.txt") as f:
        return f.read().strip()


inp = read_input().splitlines()
grid = [list(row) for row in inp]
# print(len(grid[0]))
n = 50


def part1():
    antennas = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                antennas[grid[i][j]].append((i, j))

    antinodes = set()
    for _, vals in antennas.items():
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                x_offset = vals[j][0] - vals[i][0]
                y_offset = vals[j][1] - vals[i][1]

                x1, y1 = vals[i][0] - x_offset, vals[i][1] - y_offset
                x2, y2 = vals[j][0] + x_offset, vals[j][1] + y_offset

                if 0 <= x1 < n and 0 <= y1 < n:
                    antinodes.add((x1, y1))
                if 0 <= x2 < n and 0 <= y2 < n:
                    antinodes.add((x2, y2))

    return len(antinodes)


def part2():
    antennas = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                antennas[grid[i][j]].append((i, j))

    antinodes = set()
    for _, vals in antennas.items():
        for i in range(len(vals)):
            if len(vals) > 1:
                antinodes.add(vals[i])
            for j in range(i + 1, len(vals)):
                x_offset = vals[j][0] - vals[i][0]
                y_offset = vals[j][1] - vals[i][1]

                x1, y1 = vals[i][0] - x_offset, vals[i][1] - y_offset
                while 0 <= x1 < n and 0 <= y1 < n:
                    if grid[x1][y1] == ".":
                        antinodes.add((x1, y1))
                    x1 -= x_offset
                    y1 -= y_offset

                x2, y2 = vals[j][0] + x_offset, vals[j][1] + y_offset
                while 0 <= x2 < n and 0 <= y2 < n:
                    if grid[x2][y2] == ".":
                        antinodes.add((x2, y2))
                    x2 += x_offset
                    y2 += y_offset

    return len(antinodes)


print(part1())
print(part2())
