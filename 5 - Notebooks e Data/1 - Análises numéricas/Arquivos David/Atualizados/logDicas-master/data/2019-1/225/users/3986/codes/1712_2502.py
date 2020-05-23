n=int(input("termo :"))
t=0
x=0
nk=0
si=1
v=1
while (t < n):
	t= t + 1 
	x=x + ((1 / (v * 3 ** nk)) * si)
	v= v + 2
	nk=nk +1
	si=si * (-1)
pi=x * (12**(1/2))
print(round(pi,8))