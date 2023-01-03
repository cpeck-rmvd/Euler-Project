from sympy import divisors
import itertools

# Euler Project number 21: find the sum of all "amicable numbers" below 10000
# If m is the sum n's divisors, and the sum of m's divisors is n, then m, n are amicable.

# Result = 40284

def sumDivisors(n):
    d = divisors(n)
    return sum(d) - n

res = 0

for i in range(1, 10000):
    if i == sumDivisors(sumDivisors(i)):
        res += i

print(res)

# Euler Project number 22: find the sum of the "score" for each name in file

# Result = 871198282

score_map = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
                "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
                "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
                "W": 23, "X": 24, "Y": 25, "Z": 26}

with open('names.txt') as f:
    text = f.read()

names = text.split(',')
for i in range(len(names)):
    while '"' in names[i]:
        names[i] = names[i].replace('"', '')
    while '\n' in names[i]:
        names[i] = names[i].replace('\n', '')

names.sort()
score = 0

for name in names:
    sc = 0
    for ch in name:
        sc += score_map[ch]
    score += sc * (names.index(name) + 1)
print(score)

# Euler Project number 23: Find the sum of all the positive integers
# which cannot be written as the sum of two "abundant" numbers.
# An abundant number is one whose divisors' sum exceeds the number.
# The problem statement gives us that any number over 28123 can be
# written as the sum of two abundant numbers.

# Result = 4179871

divsums = [0] * 28124
for i in range(1, 28124):
	for j in range(i * 2, 28124, i):
		divsums[j] += i
abundant = [i for (i, x) in enumerate(divsums) if x > i]

e = [False] * 28124
for i in abundant:
	for j in abundant:
		if i + j < 28124:
			e[i + j] = True
		else:
			break

print(sum(i for (i, x) in enumerate(e) if not x))

# Project Euler number 24: find the millionth lexographic permutation of
# the numbers 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Result = 2783915460

temp = itertools.islice(itertools.permutations(list(range(10))), 999999, None)
print("".join(str(x) for x in next(temp)))

# Project Euler number 25: find the first fibonnacci number with 1000 digits

fibs = [0, 1]
index = 2
f = 1
while True:
    f = fibs[index - 1] + fibs[index - 2]
    if len(str(f)) == 1000:
        print(index)
        break
    index += 1
    fibs.append(f)
