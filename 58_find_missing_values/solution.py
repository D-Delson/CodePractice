def find_missing_values(a):
    min_val, max_val = min(a), max(a)
    missing_val = [i for i in range(min_val, max_val) if i not in a]
    return missing_val

a = [3,5,6,7,8,12]
print(*find_missing_values(a), sep=',', end=' ')

    