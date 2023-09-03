def insert_element(arr: list, pos: int, new: int) -> list:
    '''
    insert the new element to the list or array in the given position

    Parameters:
    - arr (list) -> the given array
    - pos (int)  -> position
    - new (int)  -> new element

    Returns:
    - list -> returns the new list
    '''
    a1, a2  = arr[0:pos-1] , arr[pos-1:]
    a1.append(new)
    return a1 + a2
    # arr.insert(pos-1, new)
    # return arr
    
if __name__ == '__main__':
    arr = []
    len_arr = int(input('Enter the length of the array: '))
    for i in range(len_arr):
        arr.append(input('Enter the Element of the array: '))
    pos = int(input('Enter the position of the new element: '))
    new = int(input('Enter the new element: '))
    print(insert_element(arr, pos, new))
