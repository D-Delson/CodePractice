def is_palindrome(number: int) -> bool:
    n = number
    m = str(number)[::-1]
    return n == int(m)

print(is_palindrome(43456))
