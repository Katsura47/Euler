largest_chain = None

for sayi in range(1,):
    total = 0
    sayi_old = sayi
    while sayi != 1:
        if sayi % 2 == 0:
            sayi = sayi / 2
        else:
            sayi = sayi * 3 + 1
        total += 1
    if largest_chain == None:
        largest_chain = total
    elif total > largest_chain:
        largest_chain = total
        if largest_chain == 524:
            print(sayi_old)

print(largest_chain+1)