def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def same_denominator(a, b, c):
    numerator = a + c
    return numerator, b

def addition_of_fractions(a, b, c, d):
    denominator = b * d
    numerator = a * d + c * b
    return numerator, denominator

if __name__ == '__main__':
    print('Enter the values of fractions: Ex {a/b, c/d}')
    a = int(input('Enter the value of a: '))
    b = int(input('Enter the value of b: '))
    c = int(input('Enter the value of c: '))
    d = int(input('Enter the value of d: '))
    
    if b == 0 or d == 0:
        print("Denominator cannot be zero.")
    else:
        if b == d:
            numerator, denominator = same_denominator(a, b, c)
        else:
            numerator, denominator = addition_of_fractions(a, b, c, d)
        
        # Simplify the fraction
        common_divisor = gcd(numerator, denominator)
        numerator //= common_divisor
        denominator //= common_divisor

        print(f"{numerator} / {denominator}")
