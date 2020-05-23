n = float(input("numero: "))
k = 1
som = 4/1
s = -1
v = 3
while(n>k):
	som = som +(s*(4/v))
	v = v+2
	s = s*(-1)
	k=k+1
print(round(som, 8))