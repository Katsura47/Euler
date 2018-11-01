import csv

f = open("p67_triangle.txt")

lst = []
s = ""


with f as file:
    for i in csv.reader(file):
        for j in i:
            for num in j:
                if num == "\n":
                    continue
                elif num == " ":
                    continue
                s += num
                if len(s) == 2:
                    lst.append(int(s))
                    s = ""

matrix = [[lst[int(x)] for x in range(int(y*(y+1)/2),int((y+1)*(y+2)/2))] for y in range(0,100)]
print(matrix)


matrix.reverse()
a = 0
x = 1

for i in matrix[1:]:
    y = 0
    for j in i:
        matrix[x][y] = j + max(matrix[a][y], matrix[a][y + 1])
        y += 1
    a += 1
    x += 1

print(matrix[-1])
