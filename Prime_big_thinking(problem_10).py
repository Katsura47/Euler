def primeski(num):
    i = 2
    total = 0
    while i <= num/2:
        if num%i == 0:
            total += 1
            break
        i += 1
    if total == 1:
        return False
    else:
        return True
print(primeski(1))



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



# total = 0
# i = 1
# # while i < 2000000:
# #     if prime(i):
# #         total += i
# #     i += 1
# x = 4
# total = 0
# while True:
#     x += 1
#     if prime(x):
#         total += 1
#     if total == 9999 :
#         break
# print(x)
