def prime(num):
    i = 2
    total = 0
    while num/2 > i > 1:
        if num%i == 0:
            return False
        i += 1
    return True


def sum_of_divisors(num):
    i = 1
    total = 0
    while i <= num / 2:
        if num%i == 0:
            total += i
        i += 1
    return total
def amicable(num):
    cevap = sum_of_divisors(num)
    cevap_1 = sum_of_divisors(cevap)
    if cevap_1 == num and cevap != num:
        return True
    else:
        return False
print(amicable(10000))
i = 1
total = 0
while i < 10000:
    if amicable(i):
        total += i
    i += 1
print(total)