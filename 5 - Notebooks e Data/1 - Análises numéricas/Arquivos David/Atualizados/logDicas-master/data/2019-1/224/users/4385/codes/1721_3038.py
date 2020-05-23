n=float(input("digite o numero: "))
if(n<=-1 or n>=1):
	print(round(n**(1/n),2))
elif(-1<n and  n<0 or 0<n<1):
	print(round(abs(n),2))
else:
	print(round(0,2))


	