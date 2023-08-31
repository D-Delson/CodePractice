def sort_string(s):
    s = list(s)

    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] < s[j]:
                s[i], s[j] = s[j], s[i]
    return ''.join(s)

print(sort_string('delsonabce'))