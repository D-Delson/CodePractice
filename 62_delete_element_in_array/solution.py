def delete_element(arr, pos):
    del arr[pos-1]
    return arr

if __name__ == '__main__':
    print(delete_element([1,2,3,4,5,6,7], 5))