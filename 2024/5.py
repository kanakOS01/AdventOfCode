from functools import cmp_to_key
from collections import defaultdict


def read_input():
    with open("2024/input/5.txt") as f:
        return f.read().strip()


inp = read_input().split("\n\n")
orders, updates = inp[0], inp[1]
orders = orders.split("\n")
updates = updates.split("\n")
mp = defaultdict(list)
for order in orders:
    a, b = order.split("|")
    mp[int(a)].append(int(b))


def compare(a, b):
    if b in mp[a]:
        return 1
    if a in mp[b]:
        return -1


def part1():
    res = 0

    for update in updates:
        arr = list(map(int, update.split(",")))
        update_set = set()

        update_set.add(arr[0])
        flag = True
        for i in range(len(arr)):
            for j in mp[arr[i]]:
                if j in update_set:
                    flag = False
                    break
            if not flag:
                break
            update_set.add(arr[i])

        if flag:
            res += arr[len(arr) // 2]

    return res


def part2():
    res = 0
    incorrect = []

    for update in updates:
        arr = list(map(int, update.split(",")))
        update_set = set()

        update_set.add(arr[0])
        flag = True
        for i in range(len(arr)):
            for j in mp[arr[i]]:
                if j in update_set:
                    flag = False
                    break
            if not flag:
                break
            update_set.add(arr[i])

        if not flag:
            incorrect.append(arr)
            new_update = sorted(arr, key=cmp_to_key(compare), reverse=True)
            res += new_update[len(new_update) // 2]

    return res


print(part1())
print(part2())
