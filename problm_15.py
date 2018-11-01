# 20x20


# 2x2 de 9 köşe
# 1x1 de 4 köşe
# 3x3 de 16 köşe
# nxn (n+1) ** 2 tane köşe
# nxn de n kere sağa n kere alta gitcek en az
# 2n!
# n!.n!
total = 1
total_2 = 1
for i in range(1,41):
    total *= i
for i in range(1,21):
    total_2 *= i
print(total/(total_2**2))