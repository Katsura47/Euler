# Combinasyon sorusu bi nevi

from math import factorial


def comb(a,b):
    return factorial(a)/(factorial(a-b)*factorial(b))


# kaça kaç grid yapcağmz fonksiyon


def grid(n,x):
    n = n+1
    x = x+1
    return comb(n,2)*comb(x,2)




print(grid(3,2))
largest = 1000
for n in range(1,300):
    for b in range(1,300):
        yak = abs(grid(n,b) - 2*10**6)
        if yak < largest:
            largest = yak
            x,y = n,b
print(largest,x,y)
# HAHAHAHAHAHHAHAH :D ARTISLIĞINIZ KIME LAN!
