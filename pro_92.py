
def digit(sum):
    total = 0
    for k in str(sum):
        total += int(k)**2
    return total




def chain(num):
    while num != 89 and num != 1:
        num = digit(num)
    return num



i = 1
while i <200:
    a = chain(i)
    if a == 1:
        print(i)
    i += 1
        





