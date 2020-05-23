n = float(input("n "))
k = 1
som = 3
v = 2
s = 1
while(n>k):
	som = som + (4*s)/(v*(v+1)*(v+2))
	v = (v+2)
	k = k+1
	s = s*(-1)
print(round(som, 8))