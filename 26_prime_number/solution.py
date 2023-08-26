from re import L


def is_prime(number: int) -> str:
    for i in range(2, number):
        if number % i == 0:
            return 'Not a Prime'
    return 'Prime'

if __name__ == '__main__':
    print(is_prime(7))
    print(is_prime(15))

