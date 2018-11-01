
def digital_sum(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total


largest = 0
for a in range(10,100):
    for b in range(10,100):
        count = digital_sum(a**b)
        if largest < count:
            largest = count


# 99**95 = number digital_sum = 972