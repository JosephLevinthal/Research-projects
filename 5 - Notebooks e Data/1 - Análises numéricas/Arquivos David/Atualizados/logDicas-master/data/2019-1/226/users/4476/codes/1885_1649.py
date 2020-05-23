from numpy import *
s = input("s: ")
a = s.split(',')

s2 = zeros(5, dtype=int)

for i in range(size(a)):
	if a[i] == "P":
		s2[0] = s2[0] + 1
	elif a[i] == "C":
		s2[1] = s2[1] + 1
	elif a[i] == "M":
		s2[2] = s2[2] + 1
	elif a[i] == "V":
		s2[3] = s2[3] + 1
	elif a[i] == "A":
		s2[4] = s2[4] + 1
print(max(s2))
print(s2)