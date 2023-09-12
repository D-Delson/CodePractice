# values = input('Enter the four digit binary values(comma separeted): ').split(',')
# divisible_by_5 = []
# for binary in values:
#     tot = sum([int(bit) * (2**idx) for idx, bit in enumerate(list(binary)[::-1])])
#     if tot % 5 == 0:
#         divisible_by_5.append(binary)
# print(*divisible_by_5, sep=',', end=' ')


values = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        values.append(p)
print(','.join(values))