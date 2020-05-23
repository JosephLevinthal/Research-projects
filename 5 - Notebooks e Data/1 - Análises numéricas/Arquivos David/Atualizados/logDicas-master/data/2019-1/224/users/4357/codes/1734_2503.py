n=int(input("digite o numero:"))
i=0
t=0
n1=1
while(i<n):
	sinal=(-1)**i
	t= t + sinal * (4/n1)
	n1= n1 + 2
	i= i + 1
print(round(t,8))