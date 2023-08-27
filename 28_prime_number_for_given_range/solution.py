def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    start, end = map(int, input('Enter the start and end positions: ').split())
    prime_numbers = [i for i in range(start, end+1) if is_prime(i)]
    print(*prime_numbers, sep=', ', end =' ')