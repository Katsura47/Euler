def self(num):
    return num**num




i = 1
total = 0
while i < 1001:
    total += self(i)
    i += 1
print(total)
9110846700