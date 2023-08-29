def decimal_to_binary(n):
    binary = []
    while n > 0:
        digit = n % 2
        binary.append(digit)
        n //= 2
    return binary[::-1] 

print(*decimal_to_binary(11), sep='', end=' ')
