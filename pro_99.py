
# 65**65 = x 65*log65 = logx
from math import log10, e
import csv

# 2**3 = 8 3.log2 = log8

largest = 0
i = 0
with open("base_exp.txt") as input_file:
    for row in csv.reader(input_file):
        i += 1
        x = int(row[0])
        y = int(row[1])
        a = log10(x)*y
        if a > largest:
            largest = a
            largest_line = i


print(largest,largest_line)


