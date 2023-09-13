n = (input('Enter and digit: '))
v = [f'{n}'*i for i in range(1,5)]
total = sum([int(j) for j in v ])
print(total)
