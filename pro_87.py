def prime(nm):
    if nm <= 2:
        return nm == 2
    sq = nm**0.5 + 1
    i = 2
    while i < sq:
        if nm%i == 0:
            return False
        i += 1
    return True

x = 5*(10**7)

pr_lst_pw_4 = [dk for dk in range(1,85)if prime(dk)]
pr_lst_pw_3 = [c for c in range(1,369)if prime(c)]
pr_lst_pw_2 = [b for b in range(1,7073)if prime(b)]
lst = []
total = 0
for f in pr_lst_pw_4:
    for t in pr_lst_pw_3:
        for t1 in pr_lst_pw_2:
            a = f**4 + t**3 +t1**2
            if f**4 + t**3 +t1**2 <= x:
                total += 1

print(total)
# print(len(lst))
