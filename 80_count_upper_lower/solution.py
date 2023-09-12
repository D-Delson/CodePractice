n = list(input())
d = {'upper': 0, 'lower':0}
for i in n:
    if i.isupper():
        d['upper'] += 1
    elif i.islower():
        d['lower'] += 1

print('LOWERCASE:', d['lower'])
print('UPPERCASE:', d['upper'])


