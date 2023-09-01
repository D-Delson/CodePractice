def are_anagram(str1, str2):
    str1 = ''.join([i for i in str1 if i.isalpha()])
    str2 = ''.join([i for i in str2 if i.isalpha()])

    return sorted(str1) == sorted(str2)

print(are_anagram('listen', 'silent'))

