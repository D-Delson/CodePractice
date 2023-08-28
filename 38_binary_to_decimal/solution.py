def binary_to_decimal(n):
    decimal = 0
    i = 0
    while n > 0:
        digit = n % 10
        decimal += digit * (2 ** i)
        n //= 10
        i += 1
    return decimal

print(binary_to_decimal(1011))
