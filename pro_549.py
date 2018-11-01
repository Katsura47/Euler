"""The smallest number m such that 10 divides m! is m=5.
The smallest number m such that 25 divides m! is m=10.

Let s(n) be the smallest number m such that n divides m!.
So s(10)=5 and s(25)=10.
Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
S(100)=2012.

Find S(108)."""


# S(2) = 2 S(3) = 3 S(4) = 4 S(5) = 5 S(6) = 3 S(7) = 7 S(8) = 4 S(9) = 6 S(10) = 5 S(11) = 11 S(12) = 4 S(13) = 13 S(14) = 7
# prime bölenlerini bulmak şart.

from math import factorial


def prime(num):
    sq = num**0.5 + 1
    i = 2
    while i < sq:
        if num%i == 0:
            return False
        i += 1
    return True

pr_lst = [2] + [x for x in range(3,10003) if prime(x)]
print(pr_lst)

def lar_fac(num):
    for i in pr_lst:
        if prime(num):
            return num
        while num%i == 0:
            num = num / i

def s(num):
    if prime(num):
        return num
    i = lar_fac(num)
    while True:
        if factorial(i)%num == 0:
            print(i)
            break
        i += 1
    return i






total = 2
for i in range(3,101):
    print(i)
    s(i)
    print("---"*10)
