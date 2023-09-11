values = input('Enter two values with comma separated: ').split(',')
a, b = int(values[0]), int(values[1])

arr = [[i * j for j in range(b)] for i in range(a)]

    
print(arr)
    
