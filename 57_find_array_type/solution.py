def find_array_type(arr):
    if all(arr[i] < arr[i+1] for i in range(len(arr)-1)):
        return 'Ascending'
    elif all(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        return 'Decending'
    else:
        return 'Either'

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8]
    b = [9,8,7,6,5,4,3,2,1]
    c = [2,4,2,4,3,4,5,3,5]
    print(find_array_type(a))
    print(find_array_type(b))
    print(find_array_type(c))