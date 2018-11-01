def prime(num):
    i = 2
    total = 0
    while num/2 > i > 1:
        if num%i == 0:
            return False
        i += 1
    return True
from math import sqrt


def dik_ucgen(a, b):
    c = sqrt(a**2 + b**2)
    cevre = a + b + c
    return cevre
# 3 4 5
# 5 12 13
# 8 15 17
print(200*375*425)