def read_input():
    with open("2024/input/3.txt") as f:
        return f.read().strip()


inp = read_input()
nums = "0123456789"

def part1():
    res = 0
    i = 0
    while i < len(inp) - 3:
        if inp[i:i+4] == "mul(":
            a, b = 0, 0
            j = i + 4
            flag = True

            cnt = 0
            while j < len(inp) and inp[j] in nums:
                a = a * 10 + int(inp[j])
                j += 1
                cnt += 1
            if cnt <= 3 and j < len(inp) and inp[j] == ',':
                j += 1
            else:
                flag = False
            
            cnt = 0
            while j < len(inp) and inp[j] in nums:
                b = b * 10 + int(inp[j])
                j += 1
                cnt += 1

            if not(flag and j < len(inp) and inp[j] == ')' and cnt <= 3):
                i += 1
            else:
                res += a * b
                i = j + 1
        else:
            i = i + 1

    return res

def part2():
    res = 0
    i = 0
    do = True
    while i < len(inp) - 3:
        if i < len(inp) - 6 and inp[i:i+7] == "don't()":
            do = False
            i += 7
        elif inp[i:i+4] == "do()":
            do = True
            i += 4
        if do and inp[i:i+4] == "mul(":
            a, b = 0, 0
            j = i + 4
            flag = True

            cnt = 0
            while j < len(inp) and inp[j] in nums:
                a = a * 10 + int(inp[j])
                j += 1
                cnt += 1
            if cnt <= 3 and j < len(inp) and inp[j] == ',':
                j += 1
            else:
                flag = False
            
            cnt = 0
            while j < len(inp) and inp[j] in nums:
                b = b * 10 + int(inp[j])
                j += 1
                cnt += 1

            if not(flag and j < len(inp) and inp[j] == ')' and cnt <= 3):
                i += 1
            else:
                res += a * b
                i = j + 1
        else:
            i = i + 1

    return res


print(part1())
print(part2())
