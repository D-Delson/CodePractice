def replace_substring(main_str, old_substring, new_substring):
    return main_str.replace(old_substring, new_substring)

if __name__ == '__main__':
    main_str = input('Enter the string: ')
    string = input('Enter the string: ')
    sub_string = input('Enter the string to be replace')
    print(replace_substring(main_str, string, sub_string))