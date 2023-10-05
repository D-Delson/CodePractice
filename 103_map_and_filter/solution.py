li = [i for i in range(1,11)]
new_li = map(lambda x : x ** 2 , filter(lambda x : x % 2 == 0, li))
print(list(new_li))