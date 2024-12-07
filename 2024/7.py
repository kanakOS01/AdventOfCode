def read_input():
    with open("2024/input/7.txt") as f:
        return f.read().strip()


inp = read_input().splitlines()
lines = [
    [int(inp[i].split(":")[0]), list(map(int, inp[i].split(":")[1].split()))]
    for i in range(len(inp))
]
print(len(lines))


def dfs(val, i, nums, curr):
    if i == len(nums) and curr == val:
        return True
    if i == len(nums):
        return False

    return dfs(val, i + 1, nums, curr + nums[i]) or dfs(
        val, i + 1, nums, curr * nums[i]
    )


def part1():
    res = 0
    for line in lines:
        test_val = line[0]
        nums = line[1]
        if dfs(test_val, 1, nums, nums[0]):
            res += test_val
    return res


def dfs2(val, i, nums, curr):
    if curr > val:
        return False
    if i == len(nums) and curr == val:
        return True
    if i == len(nums):
        return False

    return (
        dfs2(val, i + 1, nums, curr + nums[i])
        or dfs2(val, i + 1, nums, curr * nums[i])
        or dfs2(val, i + 1, nums, int(str(curr) + str(nums[i])))
    )


def part2():
    res = 0
    for line in lines:
        test_val = line[0]
        nums = line[1]
        if dfs2(test_val, 1, nums, nums[0]):
            res += test_val
    return res


print(part1())
print(part2())
