def reverse_a_string(string: str) -> str:
    return string[::-1]

if __name__ == '__main__':
    string = input('Enter any string: ')
    print(reverse_a_string(string))