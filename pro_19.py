def zeller_cong(day, month, year):
    if month == 1 or month == 2:
        month += 12
        year -= 1

    k = year % 100
    j = year // 100
    zeller = (day + 13*(month + 1)//5 + k + k//4 + j//4 +5*j)%7
    if zeller == 1:
        return True
    return False

day = 1
total = 0
for year in range(1901,2001):
    for month in range(1,13):
        if zeller_cong(day, month, year):
            total += 1
print(total)
