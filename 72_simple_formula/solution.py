import math

def formula(c,d,h):
    return math.sqrt((2*c*d)/h)

c, h = 50, 30
d = input('Enter the values of D: ').split(',')
ans = []
for i in range(len(d)):
    ans.append((formula(c, int(d[i]), h)))
ans = [round(x) for x in ans]
print(*ans)

