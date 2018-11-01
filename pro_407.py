"""If we calculate a2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that a2 ≡ a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a2 ≡ a (mod n).
So M(6) = 4.

Find ∑M(n) for 1 ≤ n ≤ 107."""



for a in range(6,10000):
    largest = 0
    i = 1
    while i < a:
        tot = (i**2)%a
        if largest < tot:
            largest = tot
        i += 1


print(largest)
