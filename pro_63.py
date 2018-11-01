total = 0
for a in range(0,20):
    for b in range(0,100):
        n = a**b
        if len(str(n)) == b:
            print(a, b, n)
            total += 1

print(total)