def search_element(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i+1
    return 'the element not in the array'
    # pos = arr.index(ele)
    # return pos + 1

print(search_element([1,2,3,4,5], int(3)))