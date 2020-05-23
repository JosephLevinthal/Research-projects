x=int(input("Digite o numero de repeticoes: "))
j=0
a=1
b=1/(2**0.5)
t=1/4
p=1
k=0
while(x>j):
	q=((a+b)**2)/(4*t)
	print(round(q,14))
	k=a
	a=(a+b)/2 
	b=((k*b)**0.5)
	t=t-((p*(k-a)**2))
	p=2*p
	j=j+1


	
	


	