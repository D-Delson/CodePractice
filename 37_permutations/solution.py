from math import factorial

n = int(input('Number of people: '))
r = int(input('Number of seats: '))
print(factorial(n) // factorial(n-r) )