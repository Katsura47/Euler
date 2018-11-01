# 4 7 10 13 16 19 22 25
# 4 11 21 34

#i = 4#
# print(len(lst))

# n.3(n-1)/2 -(n-k)*3(n-k-1)/2 =





# buda az kodlu
# i = 1
# lst = []
# while True:
#     sayi = i*(3*i-1)/2
#     lst.append(sayi)
#     i += 1
#     if sayi%4==0:
#         print(sayi)
#     if sayi>10000:
#         break
# print(lst)


#p4 = 22
# p7 = 70
# p8 = 92
# p8-p7 : 92-20 = 22
# 92 +70 = 162

# from math import sqrt
# def pentagon(num):
#     n = sqrt(2/3*num+1/36)+1/6
#     if int(n) == n:
#         return True
#     else:
#         return False
#
# lst = [1]
# i = 2
# while True:
#     sayi = i * (3*i-1)/2
#     x = 0
#     lst.append(sayi)
#     while x < len(lst)-1:
#         top = lst[-1]+lst[x]
#         fark = lst[-1] - lst[x]
#         x += 1
#         if pentagon(fark) and pentagon(top):
#             x = None
#             break
#     i += 1
#     if x == None:
#         break
# print(fark)
# print(i-1)
def factor(num):
    i = 1
    total = 1
    while i <= num:
        total *= i
        i += 1
    return total

def dig_fac(num):
    s = str(num)
    total = 0
    for i in s:
        total += factor(int(i))
    if total == num:
        return True
    else:
        return False
total = 0
i = 10
while True:
    if dig_fac(i):
        total += i
    i += 1
    if i > 1000000:
        break
print(total)