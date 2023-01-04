from fractions import Fraction
from itertools import permutations
import math
import functools

# Decorator to print the runtime of a function

from time import monotonic

def record_time(function):
    def wrap(*args, **kwargs):
        start_time = monotonic()
        function_return = function(*args, **kwargs)
        print(f"Run time {monotonic() - start_time} seconds")
        return function_return
    return wrap

# Euler Project number 31: Find the number of ways £2 can be made using any number
# of coins where each coin in [1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p)]

# Result = 73682

ways = [1] + [0] * 200
for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
	for i in range(len(ways) - coin):
		ways[i + coin] += ways[i]
print(ways[-1])

# Euler Project number 32: Find the sum of all products whose
# multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital

# Result = 30424

a = []
l = list(permutations(range(1, 10)))
for p in l:
    a.append(list(p))
r = []
for p in a:
    if (10 * p[0] + p[1]) * (100 * p[2] + 10 * p[3] + p[4]) == 1000 * p[5] + 100 * p[6] + 10 * p[7] + p[8]:
        r.append(1000 * p[5] + 100 * p[6] + 10 * p[7] + p[8])
print(sum(list(set(r))))

# Euler Project number 33: find the denominator of the reduced fraction
# for the product of the four unique fractions "XY" / "YZ" for some nonzero
# digits X, Y, and Z having XY / YZ = X / Z

# Result = 100

res = []
for i in range(11, 99):
    for j in range(i + 1, 100):
        if j % 10:
            if i / j == int(str(i)[0]) / int(str(j)[1]) and str(i)[1] == str(j)[0]:
                res.append([i, j])
iprod = 1
jprod = 1
for pair in res:
    iprod *= pair[0]
    jprod *= pair[1]
f = Fraction(iprod, jprod)
print(str(f).split('/')[1])

# Euler Project number 34: Find the sum of all numbers which are equal
# to the sum of the factorial of their digits

# Result = 745943

def factorial_digit_sum(n):
	result = 0
	while n >= 10000:
		result += sum_leading_zeros[n % 10000]
		n //= 10000
	return result + sum_no_leading_zeros[n]

sum_leading_zeros = [sum(math.factorial(int(c)) for c in str(i)) for i in range(10000)]
sum_no_leading_zeros = [sum(math.factorial(int(c)) for c in str(i).zfill(4)) for i in range(10000)]

print(sum(i for i in range(3, 10000000) if i == factorial_digit_sum(i)))

# Euler Project number 35: count the number of circular primes below 1 million

# Result = 1140

@functools.cache
def isPrime(num):
    for factor in range(3,int(math.sqrt(num)),2):
        if num % factor == 0: return False
    return True

res = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
for i in range(101, 1000000):
    if "0" in str(i): continue
    t = int(str(i)[-1] + str(i)[:-1])
    while isPrime(t):
        if t == i:
            res.append(t)
            break
        else:
            t = int(str(t)[-1] + str(t)[:-1])
print(len(res))
