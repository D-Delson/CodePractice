def sum_array(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

print(sum_array([1,2,3,4,5]))