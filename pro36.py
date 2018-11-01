def palindromic(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


i = 1
total = 0
while i < 1000000:
    bn = bin(i)[2:]
    if palindromic(i) and palindromic(bn):
        total += i
    i += 1


print(total)