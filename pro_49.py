def prime(num):
    i = 2
    total = 0
    num1 = num
    while i <= num1:
        if num%i == 0:
            total += 1
            break
        else:
            num1 = num / i
        i += 1
    if total == 1:
        return False
    else:
        return True



def perm(num):
    pass
    # num 4 basamaklı bir sayı





lst = [0 for i in range(20000)]
i = 1000
while i < 10000:
    if prime(i):
        lst[i] = 1
    i += 1
lst1 = []
i = 0
for prime in lst:
    if prime == 1:
        x = i + 3330
        y = i + 6660
        total = 0
        if lst[x] == 1 and lst[y] == 1:
            for s in str(i):
                if s in str(x) and s in str(y):
                    total += 1
        if total == 4:
            lst1.append((i, x, y))
    i += 1

print(lst1)
296962999629
