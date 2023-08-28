def max_of_handshakes(no_of_people):
    return (no_of_people * (no_of_people - 1)) / 2

if __name__ == '__main__':
    number_of_people = int(input('Enter the number of people in the room: '))
    print(max_of_handshakes(number_of_people))