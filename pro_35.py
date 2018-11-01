




def prime(num):
    if num %6 == 1 or num %6 == 5:
        sqr = num**0.5
        i = 2
        while i <= sqr:
            if num%i == 0:
                return False
            i += 1
        return True
    return False



n = 3
is_prime = 1
total = 1
while True:
    for i in range(1,4):
        a = n*n - i*(n-1)
        if prime(a):

            is_prime += 1
    total += 4 
    if (is_prime/(total))*100 < 10:
        print(n)
        break
    n += 2
    
