n=int(input("Entrada: "))
d=0
y=1
e=1
so=0
t=0
while(t<n):
	so=so+((12)**(1/2))*((-1)/(y * (3**d))*((-1)**e))
	y=y+2
	d=d+1
	e=e+1
	t=t+1
print(round(so,8))