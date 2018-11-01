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
print(carp(120))


# 120=
# 2**3 * 3**1 * 5**1
# 60=
# 2**2 * 3 * 5
# 360
# 2**3 * 3**2 * 5 * 7
# 840
# 2**3 * 3**1 * 5 * 7
# 2520
# 2**3 3**2 5**1 * 7
i = 2
while True:
    if carp(i) > 40:
        print("-----"*20)
        print("sayının kendisi", i)
        print("çarpan sayısı", carp(i))
        print("-----" * 20)
        break
    i += 2