
def pandig(num):
    lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    nums = str(num)
    total = 0
    for s in nums:
        if s in lst:
            lst.remove(s)
            total += 1
    if total == 9:
        return True
    return False

lst = []
for i in range(2,200000):
    s = ""
    scala = 0
    while True:
        scala += 1
        s += str(i*scala)
        if len(s) >= 9:
            break
    if pandig(s) and len(s) == 9:
        lst.append(int(s))
lst = sorted(lst)
print(lst)
# Oldu





