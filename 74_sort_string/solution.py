import string


string_val = input('Enter the strings: ').split(',')

for i in range(len(string_val)):
    for j in range(i+1, len(string_val)):
        if string_val[i] > string_val[j]:
            string_val[j], string_val[i] = string_val[i], string_val[j]

print(*string_val, sep=',', end=' ')