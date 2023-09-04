def second_smallerst(array):
    sorted_arr = sorted(array)
    small_val = sorted_arr[0]
    for val in sorted_arr:
        if val != small_val:
            return val

print(second_smallerst([0,0,0,1,1,1,65,78]))