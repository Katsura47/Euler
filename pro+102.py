from csv import reader
# find the most far point distance
lst = []
i = -1
with open("triangles.txt") as input_file:
    for points in reader(input_file):
        i += 1
        lst.append([])
        for point in points:
            if len(lst[i]) == 6:
                print(lst)
                lst[i] = [int(point)]
            else:
                lst[i].append(int(point))
lst1 = []
x = -1
for i in lst:
    lst2 = []
    x += 1
    lst1.append([])
    for k in i:
        lst2.append(k)
        if len(lst2) == 2:
            lst1[x].append(lst2)
            lst2 = []
print(lst1)




def to_origin(point):
    x = point[0]
    y = point[1]
    distance = x**2 + y**2
    return distance
# our triangle with A(-340,495), B(-153,-910), C(835,-947)
def to_point(p1,p2):
    distance = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    return distance
def farest(p1,p2,p3):
    d1 = to_origin(p1)
    d2 = to_origin(p2)
    d3 = to_origin(p3)
    d4 = max(d1,d2,d3)
    if d4 == d1:
        return p1
    elif d4 == d2:
        return p2
    elif d4 == d3:
        return p3
def lineslope(p):
    if p[0] != 0:
        m = abs(p[1]/p[0])
    else:
        return False
    return m

def slopeline(p1,p2):
    dy = p1[1]-p2[1]
    dx = p1[0]-p2[0]
    if dx != 0:
        return abs(dy/dx)
    return False
total = 0
for points in lst1:
    frst = farest(points[0],points[1],points[2])
    points.remove(frst)
    m1 = lineslope(frst)
    m2 = slopeline(frst,points[0])
    m3 = slopeline(frst,points[1])
    if False in (m1,m2,m3):
        print("0",points,frst)
        continue
    if m2 <= m1 <= m3 or m2 >= m1 >= m3:
        d1 = to_point(frst,points[0])
        d2 = to_point(frst,points[1])
        d3 = to_origin(frst)
        if d1 <= d3 <= d2 or d1 >= d3 >= d2 or (d3 < d1 and d3 < d2):
            total += 1




# Just Wait For Now!
print(total)