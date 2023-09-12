n = list(input())
d = {'digits':0, 'letters': 0}

for i in n:
    if i.isalpha():
        d['letters'] += 1
    elif i.isdigit():
        d['digits'] += 1

print('LETTERS: ', d['letters'])
print('DIGITS: ', d['digits'])

