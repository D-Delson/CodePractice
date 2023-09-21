def seven_divisibles(n):
    i = 0
    while i < n:
        j = i
        i = i + 1
        if j % 7 == 0:
            yield j

for number in seven_divisibles(100):
    print(number, end =',')