import itertools
import math

# Decorator to print the runtime of a function

from time import monotonic

def record_time(function):
    def wrap(*args, **kwargs):
        start_time = monotonic()
        function_return = function(*args, **kwargs)
        print(f"Run time {monotonic() - start_time} seconds")
        return function_return
    return wrap

# Project Euler number 26: Find the value of d < 1000 for which 1/d
# contains the longest recurring cycle in its decimal fraction part.

# Result = 983

def reciprocal_cycle_len(n):
	seen = {}
	x = 1
	for i in itertools.count():
		if x in seen:
			return i - seen[x]
		else:
			seen[x] = i
			x = x * 10 % n
print(max(range(1, 1000), key=reciprocal_cycle_len))

# Euler Project number 27: Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes
# for consecutive values of n, starting with n = 0.

# Result = -59231

def isPrime(num):
    prime = True
    if num < 2: return False
    if num == 2: return True
    for factor in range(3,int(math.sqrt(num)),2):
        if num % factor == 0: prime = False
    return prime

def testEquation(a,b):
    n = 0
    while True:
        test = n**2 + a*n + b
        if isPrime(test): n += 1
        else: break
    return n


best = 0
besta = 0
bestb = 0
for a in range (-1000,1001):
    for b in range (-1000,1001):
        c = testEquation(a,b)
        if c > best: best, besta, bestb = c, a, b

print(besta*bestb)

# Euler Project number 28: the sum of the numbers on the diagonals
# in a 1001 by 1001 spiral matrix

# Result = 669171001

print(sum(4 * i * i - 6 * (i - 1) for i in range(3, 1002, 2)) + 1)

# Euler Project number 29: find the number of distinct terms in the sequence
# generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100

# Result = 9183

print(len(set([a**b for a in range(2, 101) for b in range(2, 101)])))

# Euler Project number 30: Find the sum of all the numbers that can be written
# as the sum of fifth powers of their digits

# Result = 443839

print(sum(i for i in range(2, 1000000) if i == sum(int(c)**5 for c in str(i))))
