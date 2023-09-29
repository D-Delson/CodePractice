def printMaxLength(s1, s2):
    a = len(s1)
    b = len(s2)
    if a > b:
        print(s1)
    elif b > a:
        print(s2)
    else:
        print(s1)
        print(s2)

s1 = 'delson'
s2 = 'elonmusk'

printMaxLength(s1,s2)