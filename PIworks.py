import csv
f = open("triangle.txt")

lst = []
s = ""

def is_prime(p):
    sq = p**0.5 + 1
    for i in range(2, int(sq)):
        if p%i == 0:
            return False
    return True


# Taking İnput from file to a list.
with f as file:
    for i in csv.reader(file):
        for j in i:
            ls = j.split()
            for num in ls:
                lst.append(int(num))

# converting that list to a triangular shape.
matrix = [[lst[int(x)] for x in range(int(y*(y+1)/2),int((y+1)*(y+2)/2))] for y in range(0,15)]
# For never choosing prime
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if is_prime(matrix[i][j]):
            matrix[i][j] = -15000

matrix.reverse() # Starting from bottom
a = 0
x = 1

for i in matrix[1:]:
    y = 0
    for j in i:
        matrix[x][y] = j + max(matrix[a][y], matrix[a][y + 1])
        y += 1
    a += 1
    x += 1

print(*matrix[-1])
