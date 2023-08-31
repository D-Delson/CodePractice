def remove_brackets(expression):
    brackets = ['(', ')', '[',']','{','}']

    e = [char for char in expression if char not in brackets]
    return ''.join(e)

print(remove_brackets('(a+b)^2=(a^2)+(b^2)+2ab'))