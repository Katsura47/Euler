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


i = 3
lst = [2]
while i < 100:
    if prime(i):
        lst.append(i)
    i += 1
print(len(lst))
print(lst[-5:])
#56606581 son 4 prime ın çarpımı
# 25 in 4 lü comb = 12650
# 25 tane 100 den küçük prime var
# 3204305012509561 = son 4 prime ın çarpımının karesi 160022500 buda bu kadar comb eder.(12650*12650*


def combin(num,num1):
    return factor(num)/(factor(num1)*factor(num-num1))
def factor(num):
    i = 1
    total = 1
    while i <= num:
        total *= i
        i += 1
    return total


