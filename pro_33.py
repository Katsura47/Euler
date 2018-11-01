lst = []
for a in range(10,100):
    for b in range(a+1,100):
        first_nmb = a/b
        a_s = str(a)
        bs = str(b)
        if a_s[0] == bs[0]:
            a_i = int(a_s[1])
            b_i = int(bs[1])
        elif a_s[0] == bs[1]:
            a_i = int(a_s[1])
            b_i = int(bs[0])
        elif a_s[1] == bs[0]:
            a_i = int(a_s[0])
            b_i = int(bs[1])
        elif a_s[1] == bs[1]:
            a_i = int(a_s[0])
            b_i = int(bs[0])
        else:
            a_i = 1
            b_i = -1
        if b_i == 0 or a%10 == 0:
            continue
        if a_i / b_i == first_nmb:
            lst.append((a,b))
print(lst)
