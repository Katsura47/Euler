
a = 1
b = 1
total = 0
while True:
    c = a + b
    a = b
    b = c
    total += 1
    if len(str(c)) == 1000:
        break
print(c)
print(total)
