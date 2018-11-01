from math import sqrt

import timeit

start = timeit.default_timer()
def p(a):
    return a*(3*a-1)/2

def add(a, b):
    p_t = p(a) + p(b)
    t = sqrt(2*p_t/3 + 1/36) +1/6
    if int(t) == t:
        return True
    return False

def sb(a, b):
    p_f = abs(p(a) - p(b))
    f = sqrt(2*p_f/3 + 1/36) +1/6
    if int(f) == f:
        return True
    return False

k = False
for a in range(1, 3000):
    for b in range(1, 3000):
        if a == b:
            continue
        if add(a, b) and sb(a, b):
            print(abs(p(a)-p(b)))
            k = True
            break
    if k:
        break

stop = timeit.default_timer()

print(stop - start)

# başkasının kod
# def pentagonal():
#     data = set()
#     for i in range(1,3000):
#         data.add(i*(3*i-1)//2)
#     return data
#
# p_numbers = pentagonal()
# for i in p_numbers:
#     for j in p_numbers:
#         if i - j in p_numbers and i+j in p_numbers:
#             print(i,j)
# print("Done!")
