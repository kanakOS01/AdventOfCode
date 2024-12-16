from heapq import heapify, heappop, heappush


def read_input():
    with open("2024/input/16.txt") as f:
        return f.read().strip()


inp = read_input().split("\n")
# inp = """###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############""".split("\n")
grid = [list(map(str, i)) for i in inp]
n = len(grid)


# go from s to e
# bfs with heap
# djikstra's
def part1():
    s, e = None, None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "S":
                s = (i, j)
            elif grid[i][j] == "E":
                e = (i, j)

    res = 0
    mn_heap = [(0, s, (0, 1))]
    vis = set([(s, (0, 1))])

    while mn_heap:
        cost, (i, j), (di, dj) = heappop(mn_heap)
        vis.add(((i, j), (di, dj)))
        choices = [
            (cost + 1, i + di, j + dj, di, dj),
            (cost + 1000, i, j, dj, -di),
            (cost + 1000, i, j, -dj, di),
        ]

        if (i, j) == e:
            res = cost
            break

        for ncost, ni, nj, ndi, ndj in choices:
            if grid[ni][nj] == "#":
                continue
            if ((ni, nj), (ndi, ndj)) in vis:
                continue

            heappush(mn_heap, (ncost, (ni, nj), (ndi, ndj)))

    return cost


def part2():
    pass


print(part1())
print(part2())
