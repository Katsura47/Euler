"""Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained."""


# x2 - Dy2 = 1
# x y D tam sayı
# (x-1)*(x+1) = Dy2

# x2 - 1 -dy2 = 0
# xy(dy - 1) = 1
# d = (x2 -1)/y2

def equ(d, y):
    x = (d*y**2+1)**0.5
    return x

# en büyük x için d değerleri en az olsun
for d in range(1,1000):
    lst = []
    for y in range(1,1000):
        if int(equ(d, y)) == equ(d, y):
            lst.append(d)
            k = equ(d,y)
print(lst)
print(k)

