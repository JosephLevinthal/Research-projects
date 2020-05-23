x=float(input("x: "))
i=1
soma=0

while(i>0):
	soma=soma*(x*((-1)**i))*((x**i)/i)
	i=i+1
print(round(soma,10))