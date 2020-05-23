n = float(input("n "))
k = 1
som = 1
f = 3
v = 1
s = -1
while(n>k):
	som = som+(s*(1/(f*3**v)))
	f = f +2
	v = v +1
	s = s*(-1)
	k = k+1
result = 12**0.5*som
print(round(result, 8))
