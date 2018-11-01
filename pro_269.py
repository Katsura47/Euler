# A root or zero of a polynomial P(x) is a solution to the equation P(x) = 0.
# Define Pn as the polynomial whose coefficients are the digits of n.
# For example, P5703(x) = 5x3 + 7x2 + 3



def poly(inde, x):
    k = 0
    total = 0
    for i in str(inde):
        k += 1
        total += int(i)*x**(len(str(inde))-k)
        if k == len(str(inde)):
            break
    return total


# p575(x) = 5x^2 + 7x +5

# şimdi abi aslında ne yapcan bilinmi bir tane bunu sıfırdan küçük yapan değer a bir tane büyük yapan değer b al
# sonra for num in range(a, b) yap eğer bu arada bir 0 bulursan vardır demekki integer root yoksa yoktr.:D
# meselaşu p5703 e bakak
lst_nega = []
lst_pos = []
i = -1
while True:
    lst_nega.append(i)
    lst_pos.append(-i)
    i -= 1
    if i == -2000:
        break



# The a value is index of our polynom and this func will return tuple as poly_a(tuple[0])<0 and poly_a(tuple[1])>0 so we can minimize the values
# that we can look
def rang(a):
    x = None
    k = None
    for i in lst_nega:
        if poly(a,i) < 0:
            x = i
            break
    for i in lst_pos:
        if poly(a, i) > 0:
            k = i + 1
            break
    if x == None or k == None:
        return (0, 0)
    return range(x, k)

# bak bunu hepsi için yaparsan belki güzel şeyler olr :D
total = 0
for i in range(1,100000):
    for x in rang(i):
        if poly(i, x) == 0:
            total += 1
print(total)
