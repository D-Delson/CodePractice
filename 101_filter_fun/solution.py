li = [i for i in range(1,11)]
new_list = filter(lambda x : x % 2 ==0, li)
print(list(new_list))