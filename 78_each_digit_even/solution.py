a = int(input('Enter the starting point(1000 - to 9998): '))
b = int(input('Enter the ending point(1001 - to 9999): '))

for i in range(a, b):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) %  2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        print(int(s), end=',')
