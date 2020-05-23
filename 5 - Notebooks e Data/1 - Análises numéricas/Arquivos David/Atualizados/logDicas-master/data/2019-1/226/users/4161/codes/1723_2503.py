n = int(input("serie: "))
pi = 0
t = 0
while (t<n):
	if (t%2 == 0):
		pi = pi + 4/(1 + 2*t)
		t = t + 1
	else:
		pi = pi - 4/(1 + 2*t)
		t = t + 1
print(round(pi, 8))