def digitsum(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total


def prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    sq = num**0.5 + 1
    i = 1
    while i <= sq:
        if num%i == 0:
            return False
    return True



def harshad(num):
    num1 = num
    while len(str(num)) >= 1:
        if not int(num)%digitsum(int(num)) == 0 and not prime(num1):
            return False
        num = str(num)[0:-1]
    return True

i = 1
while i<=10000:
    if prime(i):
        i = int(str(i)[0:-1])



