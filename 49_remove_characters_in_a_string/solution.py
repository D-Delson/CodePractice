def remove_character(string):
    all_chars = [chr(i) for i in range(32, 127) if not chr(i).isalpha()]
    new_str = [char for char in string if char not in all_chars]
    return ''.join(new_str)


print(remove_character('@3$%%*$&dgifie&$*&^$'))