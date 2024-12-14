def read_input():
    with open("2024/input/14.txt") as f:
        return f.read().strip()
    

inp = read_input().split('\n')

poss = []
vels = []
for i in inp:
    i = i.split(' ')
    pos = i[0][2:].split(',')
    poss.append((int(pos[0]), int(pos[1])))
    vel = i[1][2:].split(',')
    vels.append((int(vel[0]), int(vel[1])))

n = len(inp)
print(n)
r, c = 103, 101
 

def part1():
    for (i, pos), vel in zip(enumerate(poss), vels):
        x = (pos[0] + 100 * vel[0]) % c
        y = (pos[1] + 100 * vel[1]) % r
        poss[i] = (x, y)
    

    q1 = q2 = q3 = q4 = 0
    for x, y in poss:
        if x < c//2 and y < r//2:
            q1 += 1
        elif x > c//2 and y < r//2:
            q2 += 1
        elif x < c//2 and y > r//2:
            q3 += 1
        elif x > c//2 and y > r//2:
            q4 += 1

    return q1 * q2 * q3 * q4
    

def part2():
    pass


print(part1())
print(part2())