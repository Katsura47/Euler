
i = 1
while True:
    dokuz = 0
    total = 0
    a = 2*i
    b = 3*i
    c = 4*i
    d = 5*i
    e = 6*i
    for s in str(i):
        if s in str(a) and s in str(b) and s in str(c) and s in str(d) and s in str(e):
            total += 1
            if int(s) == 9:
                dokuz += 1
    if dokuz < 2:
        if len(str(i)) == total:
            break
    i += 1
print(i)
