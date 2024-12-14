import functools


def read_input():
    with open("2024/input/13.txt") as f:
        return f.read().strip()
    

inp = read_input().split('\n\n')
# inp = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279""".split('\n\n')

n = len(inp)
print(n)
buttons = []
prizes = []
prizes2 = []
for i in inp:
    lines = i.split('\n')
    line = lines[0][10:].split(', ')
    a = (int(line[0][2:]), int(line[1][2:]))
    line = lines[1][10:].split(', ')
    b = (int(line[0][2:]), int(line[1][2:]))
    line = lines[2][7:].split(', ')
    prize = (int(line[0][2:]), int(line[1][2:]))

    buttons.append((a, b))
    prizes.append(prize)
    prizes2.append((prize[0] + 10000000000000, prize[1] + 10000000000000))
    


## TAKING TOO MUCH TIME
# is something wrong?
# is it simply bad?
@functools.lru_cache
def dfs(ax, ay, bx, by, px, py, ca, cb):
    if (px, py) == (0, 0):
        return 0
    if px < 0 or py < 0 or ca > 100 or cb > 100:
        return float("inf")
    
    ch1 = 3 + dfs(ax, ay, bx, by, px-ax, py-ay, ca+1, cb)
    ch2 = 1 + dfs(ax, ay, bx, by, px-bx, py-by, ca, cb+1)

    return min(ch1, ch2)

def part1():
    res = 0
    for i in range(n):
        ax, ay = buttons[i][0]
        bx, by = buttons[i][1]
        px, py = prizes[i]
        tmp = dfs(ax, ay, bx, by, px, py, 0, 0)
        if tmp < float("inf"):
            res += tmp
    return res
    

def part2():
    res = 0
    for i in range(n):
        ax, ay = buttons[i][0]
        bx, by = buttons[i][1]
        px, py = prizes2[i]
        tmp = dfs(ax, ay, bx, by, px, py, 0, 0)
        if tmp < float("inf"):
            res += tmp
    return res


print(part1())
print(part2())