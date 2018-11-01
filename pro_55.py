
def palinrome(nm):
    return str(nm) == str(nm)[::-1]

def ters(nm):
    return int("".join(str(nm)[::-1]))



def lychrel(num):
    total = 1
    num = num + ters(num)
    while True:
        if palinrome(num):
            return False
        else:
            num = num +ters(num)
            total += 1
            if total >= 51:
                return True
tot = 0
for i in range(1,10001):
    if lychrel(i):
        tot += 1

print(tot)


