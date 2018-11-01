from math import factorial


def comb(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))


print(comb(23,10))

n = 1
lst = []
total = 0
while n <=100:
    n1 = int(n/2) + 1
    for r in range(1,n):
        if comb(n,r) > 10**6:
            total += 1
    n += 1
print(total)