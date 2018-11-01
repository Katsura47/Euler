dcr = {"A":"B","C":"D","B":"A","D":"C"}
# n*(n+1)/2 = 1 işlem
# for i in range(1, n):
#   tot += i
# = n işlem arada iyi fark var
# soruları da böyle çözmek gerek.

dcr[19] = dcr.get(10,0)+2
print(dcr)

import time
s=time.time()

dct = {}
lst = [[(i**2 + j**2)**0.5 for i in range(1, 400)]for j in range(1,400)]

for i in lst:
    for j in i:
        if int(j) == j:
            p = lst.index(i) + i.index(j) + 2 + j
            dct[p] = dct.get(p, 0) + 1

for i in dct.items():
    if i[1] >= 10:
        print(i)

print(time.time()-s)

# import time
# from math import gcd
# from statistics import mode
#
# start = time.time()
#
#
# def triples(num):
#     trips = []
#     for m in range(2, int(num / 2)):
#         for n in range(1, int(num / 2)):
#             if m > n > 0:
#                 a = (m ** 2 - n ** 2)
#                 b = 2 * m * n
#                 c = m ** 2 + n ** 2
#                 if (gcd(a, c) == 1):
#                     trips.append([a, b, c])
#     return trips
#
#
# def non_primitive(num_list):
#     non_trips = []
#     for k in range(2, 50):
#         for i in num_list:
#             non_trips.append(list(map(lambda x: k * x, i)))
#     return non_trips
#
#
# def perimeter(num_list):
#     sums = []
#     for w in num_list:
#         s = sum(w)
#         if s <= 1000:
#             sums.append(s)
#     print(mode(sums))
#
#
# perimeter(non_primitive(triples(30)))
#
# end = time.time()
# print(end - start)
