from math import sqrt


def penta(n):
    return n*(3*n-1)/2

a = sqrt(2)
b = sqrt(3)
for i in range(285,1165165000):
    k = penta(i)
    he = (sqrt(k + 1/8) + 1/(sqrt(8)))/a
    if int(he) == he:
        print(he*(2*he-1))
        print(penta(i))
        print("-"*40)
        break




# i = 286
# while True:
#     x = tri(i)
#     pe = (sqrt(2*x + 1/12) + 1/sqrt(12))/b
#     he = (sqrt(x + 1/8) + 1/(sqrt(8)))/a
#     if int(pe) == pe:
#         print(i)
#         break
#     i += 1


