def prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    i = 2
    num2 = num**0.5 + 1
    total = 0
    while i <= num2:
        if num%i == 0:
            total += 1
            break
        i += 1
    if total == 1:
        return False
    else:
        return True

def trunc(num):
    if not prime(num) or not prime(int(str(num)[0])) or not prime(int(str(num)[-1])):
        return False
    s = str(num)
    for i in range(1,len(s)):
        # start to take away from start
        a = int(s[i:])
        # start to take away from last
        b = s[0:i]
        if not prime(a) or not prime(int(b)):
            return False

    return True

i = 10
count = 0
total = 0
while True:
    if trunc(i):
        print(i)
        count += 1
        total += i
    if count == 11:
        break
    i += 1
print(total)
