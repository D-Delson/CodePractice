n = int(input('Enter the depth of the pyramid: '))
for i in range(n):
    #print spaces
    for _ in range(n-i-1):
        print(' ', end='')
    #print increasing number
    for j in range(0,i+1):
        print(j+1, end='')
    #print decreasing number
    for k in range(i+1,1,-1):
        print(k-1, end='')
    #next line
    print()