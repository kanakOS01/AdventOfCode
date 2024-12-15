def read_input():
    with open("2024/input/15.txt") as f:
        return f.read().strip()


inp = read_input().split("\n\n")
# inp = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<""".split("\n\n")
# inp = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""".split("\n\n")

warehouse = [list(map(str, i)) for i in inp[0].split("\n")]
moves = inp[1]
n = len(warehouse)


def dis(robot, move):
    for i in range(n):
        for j in range(n):
            if (i, j) == robot:
                print("@", end=" ")
            else:
                print(warehouse[i][j], end=" ")
        print()
    print(move)


def part1():
    robot = None
    for i in range(n):
        for j in range(n):
            if warehouse[i][j] == "@":
                warehouse[i][j] = "."
                robot = (i, j)

    for move in moves:
        if move == "\n":
            continue
        i, j = robot
        if move == "^":
            di, dj = -1, 0
        elif move == "v":
            di, dj = 1, 0
        elif move == "<":
            di, dj = 0, -1
        elif move == ">":
            di, dj = 0, 1

        ni, nj = i + di, j + dj

        if warehouse[ni][nj] == ".":
            robot = (ni, nj)
        elif warehouse[ni][nj] == "O":
            while warehouse[ni][nj] == "O":
                ni, nj = ni + di, nj + dj

            if warehouse[ni][nj] == ".":
                while (ni, nj) != (i, j):
                    warehouse[ni][nj] = warehouse[ni - di][nj - dj]
                    ni, nj = ni - di, nj - dj

                robot = (i + di, j + dj)

    res = 0
    for i in range(n):
        for j in range(n):
            if warehouse[i][j] == "O":
                res += 100 * i + j

    return res


def part2():
    pass


print(part1())
print(part2())
