"""Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
The last "_" must be 0 else it will not be integer square.so the problem will decrease to 1_2_3_4_5_6_7_8_9.
"""



from math import sqrt


a = 10203040506070809

b = 19293949596979899

print(sqrt(a),sqrt(b))

def form(num):
    x = 0
    for i in range(2,18,2):
        if int(str(num)[i]) - int(str(num)[x]) != 1:
            return False
        x = i
    return True

num = 11263342566178816
print(len(str(num)))
print(form(11263342566178816))
x = 0
for i in range(2,18,2):
    print(int(str(num)[i]) - int(str(num)[x]))
    x = i






for i in range(int(sqrt(a)),int(sqrt(b)+1)):
    c = i*i
    if form(c):
        print(c)
        break

