def spiral(size):
    total = 0
    for i in range(3, size + 1,2):
        pw = i*i
        total += 4*pw - (i - 1)*6
    return total

print(spiral(1001) + 1)
