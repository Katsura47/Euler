from itertools import permutations, combinations

lst =[]
print(permutations("0123456789"))
for num in  permutations("0123456789",10):
    s = ""
    for k in num:
        s += k
    lst.append(int(s))

def sub_str(num):
    lst1 = [2,3,5,7,11,13,17]
    k = 0
    for i in range(1,8):
        if not int(str(num)[i:i+3]) %lst1[k] == 0:
            return False
        k += 1
    return True
total = 0
for num in lst:
    if sub_str(num):
        total += num
print(total)
