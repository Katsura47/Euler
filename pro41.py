import itertools

def prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    i = 2
    num2 = num**0.5 + 1
    total = 0
    while i <= num2:
        if num%i == 0:
            total += 1
            break
        i += 1
    if total == 1:
        return False
    else:
        return True
def pandigital(num):
    total = 0
    for s in range(1,len(str(num))+1):
        if str(s) in str(num):
            if len(str(s)) == 2:
                total += 2
            else:
                total += 1
    if total == len(str(num)):
        return True
    else:
        return False



lst = []
s = ""
for x in itertools.permutations("1234567"):
    for n in x:
        s += n
        if len(s) == 7:
            lst.append(int(s))
            s = ""

lst.sort(reverse=True)
for i in lst:
    if prime(i):
        print(i)
        break