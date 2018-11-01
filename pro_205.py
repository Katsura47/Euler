"""Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg"""

from math import factorial
from itertools import combinations
from numpy import matrix

def comb(a, b):
    return factorial(a) / (factorial(a - b) * factorial(b))

lst = matrix([[x for x in range(1,5)]for x in range(0,9)])
print(lst)
# peter kekosu 4**9 ihtimal çıkarıyor
# Colin kekosu 6**6 ihtimal çıkarıyor
# yani toplam 4**9 * 6**6 ihtimal oluyor!
# 2 tane peter olsun 4**2
# 2 tane colin olsun 6
# 1 1
