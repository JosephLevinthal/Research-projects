from math import*
n = int(input("serie: "))
pi = 0
t = 0
while t<n+1:
	s = 1
	r = 0
	while r<=t:  
		s = s*((2*r)+1)
		r = r + 1
	pi = pi + factorial(t)/s
	t = t + 1
pi = pi*2
print(round(pi, 10))