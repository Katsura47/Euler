import numpy as np
f = open('matrix.txt', 'r')
data = []
for line in f.readlines():
    data.append(line.replace('\n','').split(' '))
    print(line)
f.close()
lst = []
for i in data:
    for j in i:
        lst1 = j.split(",")
        lst.append(lst1)
arr = np.array(lst,int)
print(arr)

x = arr[0][0]
for i in range(1, 80):
    arr[0][i] += x
    x = arr[0][i]

x = arr[0][0]
for i in range(1, 80):
    arr[i][0] += x
    x = arr[i][0]

for i in range(1,80):
    for j in range(1, 80):
        arr[i][j] += min(arr[i-1][j], arr[i][j-1])
        
print(arr[79][79])

# That's it!
