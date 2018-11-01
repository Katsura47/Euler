from math import factorial
import time
tStart = time.time()
def comb(n, r):
    total = 1
    for i in range(n-r+1,n+1):
        total *= i
    return total/factorial(r)

n = 1
total = 0
while n <=100:
    n1 = int(n/2) + 1
    for r in range(1,n):
        if comb(n,r) > 10**6:
            total += 1
    n += 1
print(total)
print("Run Time = " + str(time.time() - tStart))
# def fac(n):
#     c = fac.c.get(n)
#     if c: return c
#     c = fac(n-1)*n
#     fac.c[n] = c
#     return c
# fac.c = {0:1}
# def pfac(n,r):
#     c = pfac.c.get((n,r))
#     if c: return c
#     if n == r + 1: c = n
#     else: c = pfac(n-1,r)*n
#     pfac.c[(n,r)] = c
#     return c
# pfac.c = {}
# def choose(n, r):
#     M, m = max(n-r,r), min(n-r,r)
#     c = pfac(n,M)/fac(m)
#     return c
# sum = 4
# lastlowest = 10
# for n in range(24,100):
#     while choose(n,lastlowest) >= 1e6:
#         lastlowest -= 1
#     lastlowest += 1
#     sum += n - 2*lastlowest + 1
# print(sum)

