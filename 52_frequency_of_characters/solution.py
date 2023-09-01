def frequency_of_characters(string):
    s = {}
    for i in string:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
    return s

print(frequency_of_characters('Unity in diversity'))