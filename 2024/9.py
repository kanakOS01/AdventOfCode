def read_input():
    with open("2024/input/9.txt") as f:
        return f.read().strip()


inp = list(map(int, read_input()))
# inp = list(map(int, '2333133121414131402'))
# inp = list(map(int, '12345'))
n = len(inp)
print(n)


def part1():
    disk = []
    i = 0
    for j in range(n):
        if j % 2 == 0:
            disk = disk + [i] * inp[j]
            i += 1
        else:
            disk = disk + ["."] * inp[j]

    # print(disk)
    print(disk)
    i, j = 0, len(disk) - 1
    while i <= j:
        if disk[j] == ".":
            j -= 1
        elif disk[i] != ".":
            i += 1
        else:
            disk[i], disk[j] = disk[j], disk[i]
            i += 1
            j -= 1

    print(disk)
    res = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            break
        res += i * disk[i]

    return res


def part2():
    files = []
    spaces = []
    expanded = []
    pos = 0
    id = 0
    for i in range(n):
        if i % 2 == 0:
            files.append((pos, int(inp[i]), id))
            for j in range(int(inp[i])):
                expanded.append(id)
                pos += 1
            id += 1
        else:
            spaces.append((pos, int(inp[i])))
            for j in range(int(inp[i])):
                expanded.append(None)
                pos += 1

    for pos, cnt, id in reversed(files):
        for spaces_i, (spaces_pos, spaces_cnt) in enumerate(spaces):
            if spaces_pos < pos and spaces_cnt >= cnt:
                for i in range(cnt):
                    expanded[spaces_pos + i] = id
                    expanded[pos + i] = None
                spaces[spaces_i] = (spaces_pos + cnt, spaces_cnt - cnt)
                break

    res = 0
    for i in range(len(expanded)):
        if expanded[i]:
            res += i * expanded[i]

    return res


print(part1())
print(part2())
