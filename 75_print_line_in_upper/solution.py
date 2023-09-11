s = []
while True:
    a = input('')
    if a:
        s.append(a.upper())
    else:
        break

print(*s)