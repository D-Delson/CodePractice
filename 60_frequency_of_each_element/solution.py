def frequency_of_element(arr):
    s = {}
    for i in range(len(arr)):
        if arr[i] in s:
            s[arr[i]] += 1
        else:
            s[arr[i]] = 1
    return s

print(frequency_of_element(['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b']))