n = int(input())
i = s = 0
while i<n:
	s += 1/((1+2*i)*3**i)*(-1)**i
	i += 1
print(round((12**0.5)*s,8))