def find_ascii(character: str) -> int:
    """
    Return the ASCII value of a character.

    Parameters:
    - character (str): A single character for which the ASCII value is to be found.

    Returns:
    - int: The ASCII value of the given character.
    """
    return ord(character)  # ord() returns the ASCII value

if __name__ == "__main__":
    char = input("Enter a single character: ")

    # Check if the input is a single character
    if len(char) == 1:
        ascii_value = find_ascii(char)
        print(f"The ASCII value of '{char}' is {ascii_value}.")
    else:
        print("Please enter only a single character.")
