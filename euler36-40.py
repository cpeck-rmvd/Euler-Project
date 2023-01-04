import functools
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

# Euler Project number 36: find the sum of all numbers under 1000000
# which are palindromic both in base 10 and base 2

# Result = 872187

res = 0
for i in range(1, 1000000, 2):
    if str(i) == str(i)[::-1]:
        if str(bin(i))[2:] == str(bin(i))[2:][::-1]:
            res += i
print(res)

# Euler Project number 37: Find the sum of the only eleven primes
# that are both truncatable from left to right and right to left

# Result = 748317

@functools.cache
def isPrime(n):
    if(n > 1):
    	for k in range(2, int(math.sqrt(n)) + 1):
    		if (n % k == 0):
    			return False
    	return True
    else:
    	return False

a = []
i = 11

while len(a) < 11:
    if isPrime(i):
        t = i
        mod = len(str(i)) - 1
        while mod > 0:
            if not isPrime(i % 10 ** mod):
                break
            mod -= 1
        if mod == 0:
            while isPrime(t):
                t = t // 10
                if t == 0: a.append(i)

    i += 2

print(sum(a))

# Euler Project number 38: find the largest "pandigital" number that can
# be acquired via a concatenated product of some number.
# A pandigital number is one consisting exactly of the digits [1, 2, 3, 4, 5, 6, 7, 8, 9]
# The concatenated product for an integer n is found by concatenating:
# [1 * n, 2 * n, ... , k * n] for some integer k >= 2. It is clear that
# any number with 5+ digits cannot satisfy this, and 9 is the smallest number
# with a pandigital concatenated product, so we look in [10, 9999]

# Result = 932718654

def get_concatenated_product_if_pandigital(n):
    t = 1
    s = ''
    while len(s) < 9:
        s += str(t * n)
        t += 1
    t = int(s)
    if sorted(list(int(k) for k in s)) == [1, 2, 3, 4, 5, 6, 7, 8, 9]: return t
    else: return 0

m = get_concatenated_product_if_pandigital(9)
for i in range(10, 10000):
    m = max(get_concatenated_product_if_pandigital(i), m)
print(m)

# Euler Project number 39: find the number p, at most 1000, which has the
# most Pythagorean triplets (a, b, c) having a + b + c = p.
# A Pythagorean triplet is any three numbers (a, b, c) such that a^2 + b^2 = c^2

# Result = 840

def count_solutions(p):
	result = 0
	for a in range(1, p + 1):
		for b in range(a, (p - a) // 2 + 1):
			c = p - a - b  # c >= b
			if a * a + b * b == c * c:
				result += 1
	return result

print(max(range(1, 1001), key=count_solutions))

# Euler Project number 40: An irrational decimal fraction is created
# by concatenating the positive integers and it looks like this:
# 0.123456789101112131415161718192021...
# Find the product of the digits in this decimal at places 10^n for n in [0, 6]

# Result = 210

s = "".join(str(i) for i in range(1, 1000000))
ans = 1
for i in range(7):
	ans *= int(s[10**i - 1])
print(ans)
