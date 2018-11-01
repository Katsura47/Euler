import csv
lst = []
s = ""
with open("pro11.txt") as input_file:
    for line in csv.reader(input_file):
        for num in line:
            for word in num:
                if word != " ":
                    s += word
                    if len(s) == 2:
                        lst.append(int(s))
                        s = ""




largest = 1
matrix = [[lst[x] for x in range(20*scala,20*scala+20)] for scala in range(0,20)]

for col in range(0,16):
    for i in range(0,16):
        count = 1
        count2 = 1
        for k in range(i,i+4):
            count *= matrix[col][k]
        if count > largest:
            largest = count

# [0][0]*[1][0]
for col in range(0,20):
    for i in range(0,16):
        count = 1
        for k in range(i,i+4):
            count *= matrix[k][col]
        if count > largest:
            largest = count

# [0][0]*[1][1]*[2][2]*[3][3]
# [0][1]*[1][2]
i = 0
j = 0
sayi = 0
largest1 = 1
for row in range(0, 17):
    r = row
    for col in range(0, 17):
        count = 1
        c = col
        for x in range(0, 4):
            count *= matrix[row+x][col+x]
            sayi += 1
        if count > largest1:
            largest1 = count
print(largest1)



largest2 = 1
for col in range(0,17):
    count = 1
    count2 = 1
    for k in range(col,col+4):
        count *= matrix[col][k]
        count2 *= matrix[k][col]

    if count > largest2 or count2 > largest2:
        if count > count2:
            largest2 = count
        else:
            largest2 = count2
print(largest2)
print("--"*40)
l1 = [c for c in range(0,20)]
print(l1[:2:-1])
# row +1 col -1
# Answer is here!
for i in range(0,17):
    for j in l1[:2:-1]:
        if matrix[i][j]*matrix[i+1][j-1]*matrix[i+2][j-2]*matrix[i+3][j-3] > 4*10**7:
            print(matrix[i][j]*matrix[i+1][j-1]*matrix[i+2][j-2]*matrix[i+3][j-3])



