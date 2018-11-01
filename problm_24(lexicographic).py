i = 10000
lst1 = []

while i < 99999:
    total = 0
    for k in str(i):
        total += int(k)**4
    if total == i:
        lst1.append(total)
    i += 1
print(lst1)