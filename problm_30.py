i = 1
lst1 = []
total_tot = 0
while i < 999999:
    total = 0
    for k in str(i):
        total += int(k)**5
    if total == i:
        lst1.append(total)
        total_tot += total
    i += 1
print(lst1)
print(total_tot-1)