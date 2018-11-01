"""A set of disks numbered 1 through 100 are placed in a line in random order.

What is the probability that we have a partial derangement such that exactly 22 prime number discs are found away from their natural positions?
(Any number of non-prime disks may also be found in or out of their natural positions.)

Give your answer rounded to 12 places behind the decimal point in the form 0.abcdefghijkl."""

# First I have to num of primes between 1-100
# I will take the combination of x = C(P,22)
#
from math import factorial
from itertools import permutations


def prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    i = 2
    num2 = num ** 0.5 + 1
    total = 0
    while i <= num2:
        if num % i == 0:
            total += 1
            break
        i += 1
    if total == 1:
        return False
    else:
        return True




i = 1
lst = []
while i < 100:
    if prime(i):
        lst.append(i)
    i += 1



# There Are 25 Primes That between 1-100
# Now lets take the combination



def comb(a, b):
    return int(factorial(a) / (factorial(a - b) * factorial(b)))

def per(a, b):
    return factorial(a) / factorial(a - b)

#abi deliminator kısmında 100! olcak bikere üst taraftada bir tane comb(25,3) olacak bunlar kesn.
# ilk başta 22 prime hiç primeların yerine gelmesin 75 yerimiz var 75*74*73*.......*54
# 22 tane primedan sadece 1 tane gelsn primelk yere oda comb(22,1)*21*74*73*........*53
# 22 tane primedan sadece 2 tanesi primelk yerlere gelsınler comn(22,2)*

# mesela bunu 25 i de yerinde olcak şekilde yaparsam direk 75!/100! olur.
# mesela bunu 24 i yerinde biri olmıcak şekilde yapsam comb(25,24)*76*75! olur
# mesala bunların 23 i yerinde 2 tanesi yerinde değil şekilde yapsak ilk comb(25,23)*[n]*75! n = ? n = 75*75 + 1*75 + 1
# n i bulmak için 2 adım yapıcaz elimizde 77 yer var 75 i prime olmayan 2 tanesi prime . ilk olarak comb(2,1) yapsak
# sonra ilk olarak bir tanesi primlk yerlere gelmesn diğeri de kendi hariç bir yere gelebilir so  ===> 75*75 + 1*75 + 1 = n
#