import math
import itertools

# Euler Project number 1: get all numbers less than 1000
# that are divisible by either 3 or 5

# Result = 233168

print(sum([i for i in range(1,1000) if 0 in [i % 3, i % 5]]))

# Euler Project number 2: get sum of all even fibonacci numbers
# not exceeding 4 million

# Result = 4613732

fibs = [0, 1]
i = 2
fib = 1

while fib <= 4000000:
    fib = fibs[i - 1] + fibs[i - 2]
    fibs.append(fib)
    i += 1

print(sum([f for f in fibs if f % 2 == 0]))

# Euler Project number 3: find the largest prime factor of 600851475143

# Result = 6857

maxPrime = 0

n = 600851475143

for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        maxPrime = i
        n = n / i

print(maxPrime)

# Euler Project number 4: Find the largest palindrome made from the product of two 3-digit numbers.

# Result = 906609

pal = 0
for i in range(900, 999):
    for j in range(i + 1, 1000):
        if str(i * j) == str(i * j)[::-1]:
            pal = max(pal, i * j)
print(pal)

# Euler Project number 5: find least common multiple of all numbers 1 - 20

# Result = 232792560

"""
Intuition: the prime factorization of the LCM will consist exactly of those
numbers which are prime factors of 1 - 20. Those factors are:

2: 2
3: 3
4: 2, 2
5: 5
6: 2, 3
7: 7
8: 2, 2, 2
9: 3, 3
10: 5, 2
11: 11
12: 2, 2, 3
13: 13
14: 2, 7
15: 3, 5
16: 2, 2, 2, 2
17: 17
18: 2, 3, 3
19: 19
20: 2, 2, 5

So to make these numbers, we need four 2's, two 3's,
and one each of [5, 7, 11, 13, 17, 19]
"""

print(2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19)

# Euler Project number 6: Find the difference between the sum of the squares
# of the first one hundred natural numbers and the square of the sum.

# Result = 25164150

sumSquare = sum([i ** 2 for i in range(1, 101)])
squareSum = sum([i for i in range(1, 101)]) ** 2

print(abs(sumSquare - squareSum))

# Euler Project number 7: Find the 10,001st prime number

# Result = 104743

def nth_prime_number(n):
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list[-1]

print(nth_prime_number(10001))

# Euler Project number 8: find the largest product of 13 consecutive digits
# from very long number

# Result = 23514624000

num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

s = str(num)
m = 0
for i in range(len(s) - 13):
    p = 1
    for j in s[i:i + 13]:
        p *= int(j)
    m = max(m, p)
print(m)

# Euler Project number 9: find the product of the unique Pythagorean triplet
# (a, b, c such that a^2 + b^2 = c^2) where a + b + c = 1000

# Result = 31875000

br = False
for a in range(100, 500):
    for b in range(100, 500):
        for c in range(100, 500):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print(a * b * c)
                br = True
                break
        if br: break
    if br: break

# Euler Project number 10: Find the sum of all primes below 2 million

# Result = 142913828922

n = 2000000
arr = [False] * (n+1)
i = 2
while i ** 2 <= n:
	if not arr[i]:
		arr[i] = 'p'
		for j in range(i ** 2, n + 1, i):
			arr[j] = True
	i += 1
while i < n:
	if not arr[i]:
		arr[i]='p'
	i += 1
print(sum(k for k in range(len(arr)) if arr[k] == 'p'))

