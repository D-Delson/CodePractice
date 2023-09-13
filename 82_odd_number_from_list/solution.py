a = input('').split(',')
val = [i for i in range(len(a)) if int(a[i]) % 2 ==0 ]
print(*val)