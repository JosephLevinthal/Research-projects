x=float(input("entre com um numero real"))
k=int(input("entre com a quantida de termos da serie:"))
soma=0
i=0
while(i<k):
	soma=soma+(x**(2*i))*(-1)**i
	i=i+1
		
print(round(soma,8))