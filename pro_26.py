


# 1/17 için 1i 100 yaprom 0.0 sonra 5 defa var 0.05 150 8 0.058



def proper(dec):
    a = 1
    total = 0
    lst = [0 for i in range(10000)]
    while a%dec != 0:
        if a/dec > 1:
            lst[a] = 1
            total += 1
            a =  a%dec
        else:
            a = a*10
        if lst[a] == 1:
            break
    return total

large = 0

for i in range(1,1000):
    if large < proper(i):
        large = proper(i)
        d = i
print(large,d)

print(proper(983))


