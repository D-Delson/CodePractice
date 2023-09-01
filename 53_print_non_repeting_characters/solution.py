def non_repeting_characters(string):
    s = {}
    for i in string:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
    return ' '.join([s for s, v in s.items() if v == 1])
    
print(non_repeting_characters('Unity in diversity'))