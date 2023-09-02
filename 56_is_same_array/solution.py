def is_same_array(a, b):
    print(sorted(a))
    print(sorted(b))
    return  sorted(a) == sorted(b)

if __name__ == '__main__':
    a = []
    b = []
    l = int(input('Enter the length of a: '))
    for _ in range(l):
        a.append(input('Enter the value of the array A: '))
    for _ in range(l):
        b.append(input('Enter the value of the array B: '))
    print(is_same_array(a, b))