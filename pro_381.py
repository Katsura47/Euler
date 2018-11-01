def facto(num):
    x = num + 1
    total = 1
    for i in range(1, x):
        total *= i
    return total

def func1(p):
    total = 0
    return (facto(int((p-1)/2))%p)*(facto(int((p+1)/2))%p)%p


print(func1(5))
p = 5
total = 0
while p < 102:
    if total == 486:
        break
    total += func1(p)
    p += 1
print(total)