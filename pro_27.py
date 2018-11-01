import timeit

start = timeit.default_timer()

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
# def prime(num):
#     if num == 1 or str(num)[-1] == "5" or num <= 0:
#         return False
#     if num == 2:
#         return True
#     num1 = num
#     num2 = num1**0.5 + 1
#     i = 2
#     while i <= num2:
#         if num%i == 0:
#             return False
#         num2 = (num1/i) ** 0.5 + 1
#         i += 1
#     return True

def denk(n, a, b):
    return n**2 +a*n + b

# n**2 +a*n + b = sayı
# Denklem bu!^^
# sayının prime olmasını istiyorum
# n = 0 ---> b
# n = 1 ---> 1 + a + b
# n = 2 ---> 4 + 2*a + b
# n = 3 ---> 9 + 3*a + b
# demekki b prime olcak.
# 1 + a +b de prime olcak
largest = 0
for b in range(0,1000):
    if prime(b):
        for a in range(-b,1001):
            if not prime(1 + a + b):
                continue
            n = 0
            count = 0
            while True:
                if not prime(denk(n, a, b)):
                    break
                count += 1
                n += 1
            if count > largest:
                largest = count
                x = a*b
print(x)


stop = timeit.default_timer()

print(stop - start)
# Yes Man Yes!!!! MuHahahahahhahah
