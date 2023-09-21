from operator import itemgetter

l = []
while True:
    n = input()
    if not n:
        break
    l.append(tuple(n.split(',')))

print(sorted(l, key=itemgetter(0,1,2)))
    
    