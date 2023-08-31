def count_sum(string):
    s = list(string)
    nums = '0123456789'
    total = sum([int(i) for i in s if i in nums])
    return total

print(count_sum('12345delson'))