def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True         
n = 100
prime_numbers_list = [i for i in range(2, n) if is_prime(i)]
print(prime_numbers_list)

for i in range(len(prime_numbers_list)):
    for j in range(len(prime_numbers_list)):
        if sum([prime_numbers_list[i], prime_numbers_list[j]]) == n:
             print(prime_numbers_list[i], prime_numbers_list[j])
            
