def count_threes(n):
    count = 0
    for i in range(n+1):
        count += str(i).count('3')
    return count

print(count_threes(100))
