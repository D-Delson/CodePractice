import math
pos = [0,0]
while True:
    s = input('Enter the pos and points (UP,4): ')
    if not s:
        break
    movement = s.split(',')
    if movement[0].lower() == 'up':
        pos[0] += int(movement[1])
    elif movement[0].lower() == 'down':
        pos[0] -= int(movement[1])
    elif movement[0].lower() == 'right':
        pos[1] += int(movement[1])
    elif movement[0].lower() == 'left':
        pos[1] -= int(movement[1])
    else:
        pass

print(round(math.sqrt(pos[0] ** 2 + pos[1] ** 2)))
