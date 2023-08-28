def pyramid(rows):
    for i in range(rows):
        #print spaces
        for _ in range(rows-i-1):
            print('a', end = '')
        #print star
        for _ in range(2*i+1):
            print('*', end='')
        print()

if __name__ == '__main__':
    rows = int(input('Enter depth of the pyramid: '))
    pyramid(rows)