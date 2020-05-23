n = int(input())
i = s = 0
while i<n:
	s += 4/(1+2*i)*(-1)**i
	i += 1
print(round(s,8))