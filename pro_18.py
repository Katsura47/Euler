tri = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


lst = []
s = ""
for num in tri:
    if num == "\n":
        continue
    elif num == " ":
        continue
    s += num
    if len(s) == 2:
        lst.append(int(s))
        s = ""



"""
for(int j = 0; j < 15; j++){
    for(int i = j*(j+1)/2; i < (j+1)*(j+2)/2;i++){
        
"""
print(lst)
# 1 satır 1 elemanlı son satır 15 elemanlı
# y = 0 için sadece x = 0 y = 1 için x = 1 ve x = 2 y = 2 için 3 4 5
matrix = [[lst[int(x)] for x in range(int(y*(y+1)/2),int((y+1)*(y+2)/2))] for y in range(0,15)]

# bi altındaki birde bir altındakinin bir yanındaki ile konuşabilir


matrix.reverse()
a = 0
for i in matrix[1:]:
    x = matrix.index(i)
    for j in i:
        y = i.index(j)
        matrix[x][y] = j + max(matrix[a][y], matrix[a][y + 1])
    a += 1
print(matrix[-1])
print(matrix)









        
