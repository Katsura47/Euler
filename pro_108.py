
""""1/n = 1/x +1/y diye yazılabiliyormş x,y,n tam sayı işte bir tane n varmş 1000 tane farklı şekilde yazılabiliyor en küçüğünü bul"""

# abi çarpan sayısı 1000 i geçen en küçük sayıyı bul işte:D


#
def prime(num):
    if num == 1 or num < 0:
        return False
    if num == 2:
        return True
    sqr = num**0.5
    i = 2
    while i <= sqr:
        if num%i == 0:
            return False
        i += 1
    return True

pr_lst = [x for x in range(1,1000) if prime(x)]
def carp(num):
    s = ""
    total = 1
    for x in pr_lst:
        us = 1
        while num%x == 0:
            num = num/x
            us += 1
            s += str(x) + " "
        total *= us
    return total




# yanlş olablr ama !

# 1/n = 1/x + 1/y
# şimdi x = n den 2n+1 her sayı için denetsem sonra 1/n - 1/x = 1/y eğer y tam  sayıysa

# n = 554400 1238 farklı
total = 0
# n = 277200 1013 tane var
for n in range(100000,400001,100):
    if n%8 == 0 and n%9 == 0 and n%100 == 0:
        total = 0
        for x in range(n+1, 2*n+1):
            y = (x*n)/(x-n)
            if int(y) == y:
                total += 1
        if total > 1000:
            print(n, total)
print(total)
# To be Continued

