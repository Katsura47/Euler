a = 999
b = 999
largest_pal = 0

def palin(num):
    lst = []
    lst1 = []
    for i in str(num):
        lst.append(i)
        lst1.append(i)
    lst1.reverse()
    if lst == lst1:
        return True
    else:
        return False
lst = []
while a > 10:
    b = 999
    while b > 10:
        sayi = a*b
        if palin(sayi):
            lst.append(sayi)
            break
        b -= 1
    a -= 1
lst.sort()
print(lst[-1])


