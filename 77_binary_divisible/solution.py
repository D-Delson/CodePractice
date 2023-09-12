values = input('Enter the four digit binary values(comma separeted): ').split(',')
divisible_by_5 = []
for binary in values:
    tot = sum([int(bit) * (2**idx) for idx, bit in enumerate(list(binary)[::-1])])
    if tot % 5 == 0:
        divisible_by_5.append(binary)
print(*divisible_by_5, sep=',', end=' ')