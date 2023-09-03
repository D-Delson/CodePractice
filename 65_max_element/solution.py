def max_val(arr):
    max_val = arr[0]
    for val in arr:
        if max_val < val:
            max_val = val
    return max_val
    # return max(arr)

print(max_val([1,2,3,4,5,6,7,8]))