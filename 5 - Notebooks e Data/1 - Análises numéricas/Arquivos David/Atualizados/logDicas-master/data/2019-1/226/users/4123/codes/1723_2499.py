from math import*
k = int(input())
i = s = 0
while i < k:
	s += 1/(factorial(i))
	i += 1
print(round(s,8))