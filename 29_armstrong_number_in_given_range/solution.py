def armstrong_number(n):
    length = len(str(n))
    number = n
    total = 0
    while n > 0:
        temp = n % 10
        total += temp ** length
        n //= 10
    return number == total

if __name__ == '__main__':
    armstrong_numbers = [i for i in range(1000, 10000) if armstrong_number(i)]
    print(armstrong_numbers)
