# values = input().split(' ')
# char_val, int_val = values[0::2], values[1::2]
# net_amount = 0
# for i, c in enumerate(char_val):
#     if c.lower() == 'd':
#         net_amount += int(int_val[i])
#     else:
#         net_amount -= int(int_val[i])
# print(net_amount)

#another method
netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)




