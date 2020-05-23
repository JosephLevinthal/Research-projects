n= int(input("numero de repeticoes: "))
s=0
i=0


while(n>0):
	s= s+(12**(1/2))*((1/((2*i+1)*(3**i))))*((-1)**i)
	i=i+1
	n=n-1
print(round(s,8))