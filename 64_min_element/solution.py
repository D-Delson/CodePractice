def min_element(arr):
    min_val = arr[0]
    for val in arr:
        if val < min_val:
            min_val = val
    return min_val
    #return min(arr)


print(min_element([1,2,-3,4,5,0]))