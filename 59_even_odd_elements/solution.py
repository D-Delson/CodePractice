def even_odd_elements(arr):
    even = []
    odd = []
    for i in range(1,len(arr)):
        if arr[i] % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return (even, odd)

a = [i for i in range(1, 21)]
odd_num, even_nums = even_odd_elements(a)
print('Even Elements: ', even_nums)
print('Odd numbers: ', odd_num )

