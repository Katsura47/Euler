a = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716
"""
lst = []
s = ""
for i in a:
    if i == "\n":
        lst.append(s)
        s = ""
        continue
    else:
        s += i
print(lst)
first = None
for stuff in lst:
    if first == None:
        first = stuff[0]
    elif stuff[1] == first or stuff[2] == first:
        first = stuff[0]
last = None
for stuff in lst:
    if last == None:
        last = stuff[2]
    elif stuff[1] == last or stuff[0] == last:
        last = stuff[2]

num_lst = [3, 1, 9, 6, 8, 0, 7, 2]
my_lst = [0, 0, 0, 0, 0, 0, 0, 0]
num_ls1 = []
for i in num_lst:
    for s in lst:
        if str(i) == s[0]:
            for x in s[1:]:
                if not x in num_ls1:
                    num_ls1.append(x)
    print(i,num_ls1)
    my_lst[7-len(num_ls1)] = i
    num_ls1 = []

print(my_lst)



73162890
