n = int(input())
i = s = 0

while(i<n):
	s += 1/(1+i)**2
	i += 1
pi = (6*s)**0.5
print(round(pi,6))