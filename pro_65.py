



# kaçıncı terim istiyorsan, soruda 100.yü istemiş.
index = int(input("Enter index"))


neares = (index//3)*2


if(index%3 == 1):
    answer_a = 1
    answer_b = 1
elif(index%3 == 2):
    answer_a = 2
    answer_b = 1
else:
    answer_a = neares*2 + 1
    answer_b = neares + 1
    neares -= 2
    index = index - 3

for i in range(0, index//3 - 1):
    answer_a2 = (2*neares + 1)*answer_a + 2*answer_b
    answer_b2 = (neares + 1)*answer_a + answer_b
    answer_a = answer_a2
    answer_b = answer_b2
    neares = neares - 2

answer_a = 8*answer_a + 3*answer_b
print(answer_a)
total = 0
for i in str(answer_a):
    total += int(i)
print(total)
