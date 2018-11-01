def prime(num):
    i = 2
    num1 = num**0.5 +1
    while i <= num1:
        if num%i == 0:
            return False
        i += 1
    return True



lst = [2] + [i for i in range(3,100000)if prime(i)]



def cofac(nm):
    total = 0
    for i in lst:
        if nm == 1:
            break
        if nm%i == 0:
            while nm%i == 0:
                nm = nm/i
            total += 1
    return total

i = 1
a = 0
b = 0
c = 0
d = 0
while True:
    if cofac(i) == 4:
        a = b
        b = c
        c = d
        d = i
        if d - a == 3:
            print(a,b,c,d)
            break
    i += 1

