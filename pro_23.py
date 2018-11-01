
from math import sqrt
from itertools import combinations

def factortop(nm):
    sqr = sqrt(nm)
    total = 0
    for i in range(2,int(sqr)+1):
        if nm%i == 0:
            total += nm/i + i
    if int(sqr) == sqr:
        return total + 1 - sqr
    return total + 1



lst = []
for i in range(11, 29000):
    if factortop(i) > i:
        lst.append(i)

print(len(lst))
