def toggle_character(str):
    return  ''.join([char.lower() if char.isupper() else char.upper() for char in str])

if __name__ == '__main__':
    print(toggle_character('WorlD'))