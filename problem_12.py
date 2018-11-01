def num_of_div(num):
    i = 1
    total = 0
    while i <= num / 2:
        if num % i == 0:
            total += 1
        i += 1
    return total + 1

i = 1
while True:
    if i%2==0:
        a = i/2
        total = a*(i+1)
        if num_of_div(a)*num_of_div(i+1)>500:
            print(total)
            break
    else:
        a = (i+1)/2
        total = i*a
        if num_of_div(a)*num_of_div(i)>500:
            print(total)
            break
    i += 1

