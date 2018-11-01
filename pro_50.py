# func to find prime nums
import timeit

start = timeit.default_timer()

def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    sqr = num**0.5 + 1
    firs = 2
    while firs < sqr:
        if num % firs == 0:
            return False
        firs += 1
    return True


def next_prime(num):
    num = num + 1
    while(not prime(num)):
        num = num + 1
    return num

i = 2
total = 0
# add whole primes to find the num smaller than 10**6 (it may not be prime)
while True:
    if total + i > 1000000:
        print(i)
        break
    else:
        total += i
    i = next_prime(i)
k = 2
# start from smallest prime and sub them from number that you find and if number is became prime somewhere it's answer.
while True:
    if prime(total):
        print(total)
        break
    else:
        total = total - k
        k = next_prime(k)
# Thats pretty good to solve this stuffs
stop = timeit.default_timer()

print(stop - start)

