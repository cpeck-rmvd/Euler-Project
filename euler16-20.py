import math
import datetime

# Decorator to print the runtime of a function

from time import monotonic

def record_time(function):
    def wrap(*args, **kwargs):
        start_time = monotonic()
        function_return = function(*args, **kwargs)
        print(f"Run time {monotonic() - start_time} seconds")
        return function_return
    return wrap

# Euler Project number 16: find the sum of the digits of 2^1000

# Result = 1366

print(sum([int(i) for i in str(2 ** 1000)]))

# Euler Project number 17: find the number of letters required to write
# all the numbers 1 - 1000 in English

# Result = 21124

def to_english(n):
	if n < 20:
		return ones[n]
	elif 20 <= n < 100:
		return tens[n // 10] + (ones[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return ones[n // 100] + "hundred" + (("and" + to_english(n % 100)) if (n % 100 != 0) else "")
	elif n == 1000:
		return to_english(n // 1000) + "thousand" + (to_english(n % 1000) if (n % 1000 != 0) else "")


ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

print(sum(len(to_english(i)) for i in range(1, 1001)))

# Euler Project number 18: find maximum path through given triangle

# Result = 1074

triangle = [
	[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20, 4,82,47,65],
	[19, 1,23,75, 3,34],
	[88, 2,77,73, 7,63,67],
	[99,65, 4,28, 6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
	[ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23],
]

for i in reversed(range(len(triangle) - 1)):
	for j in range(len(triangle[i])):
		triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
print(triangle[0][0])

# Euler Project number 19: find the number of Sundays that fell on
# the first of a month during the twentieth century

# Result = 171

print(sum(1 for y in range(1901, 2001) for m in range(1, 13) if datetime.date(y, m, 1).weekday() == 6))

# Euler Project number 20: find the sum of the digits of 100!
# (100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)

# Result = 648

print(sum(int(i) for i in str(math.factorial(100))))
