passwords = input().split(',')
valid_passwords = []
for password in passwords:
    d = {
        'lower':0,
        'upper':0,
        'digit':0,
        'special_characters':0
    }
    for i in password:
        if i.islower():
            d['lower'] += 1
        elif i.isupper():
            d['upper'] += 1
        elif i.isdigit():
            d['digit'] += 1
        else:
            d['special_characters'] += 1
    
    if (len(password) >= 6) and (len(password) <= 12) and (d['lower'] >= 1) and (d['upper'] >= 1) and (d['digit'] >= 1) and (d['special_characters'] >= 1):
        valid_passwords.append(password)

print(*valid_passwords)

# import re
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print(",".join(value))