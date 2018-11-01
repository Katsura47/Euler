

def pandi(num1,num2,num3):
    tot = len(str(num1)+str(num2)+str(num3))
    if tot != 9:
        return False
    for i in range(1,10):
        i = str(i)
        if i in str(num1) or i in str(num2)or i in str(num3):
            continue
        return False
    return True




total = 0
lst = []
for i in range(1,100):
    for j in range(100,10000):
        product = i*j
        if product in lst:
            continue
        if pandi(i,j,product):
            lst.append(product)
            total += product




print(total)
