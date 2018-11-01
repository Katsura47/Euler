def prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    i = 2
    num2 = num**0.5 + 1
    total = 0
    while i <= num2:
        if num%i == 0:
            total += 1
            break
        i += 1
    if total == 1:
        return False
    else:
        return True
prime_lst = [x for x in range(1,6000) if prime(x)]

n = 9
while True:
    for p in prime_lst:
        if n < p:
            break
        else:
            if not prime(n):
                a = ((n-p)/2)**0.5
                if int(a) == a:
                    # print("sayımız:", n, "asalımız:", p, "karesi alıncak sayımız:", a)
                    comb = False
                    break
                else:
                    comb = True
    if comb:
        print(n)
        break
    n += 2
# Kaçarmı hiç!


# from math import sqrt
# from itertools import filterfalse
#
#
# def check(n):
#     for i in range(1, int(sqrt(n))):
#         if n - 2 * i**2 in primes:
#             return True
#     return False
#
#
# # find primes first
# up = 10**4 + 1
# all_num = [1] * up
# for pos, value in enumerate(all_num):
#     if pos == 1 or pos == 0 or not value:
#         continue
#     else:
#         for j in range(pos * 2, up, pos):
#             all_num[j] = 0
#
# primes = [i for i, value in enumerate(all_num) if value]
# primes.pop(0)
# primes.pop(0)
# primes = set(primes)
# composites = [i for i, j in enumerate(all_num) if not j and i % 2]
#
# n = list(filterfalse(check, composites))
# print(n)