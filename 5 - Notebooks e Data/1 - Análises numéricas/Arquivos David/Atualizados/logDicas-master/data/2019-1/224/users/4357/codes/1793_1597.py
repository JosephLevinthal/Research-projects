from numpy import*
compra=array(eval(input("digite o numero:")))
desconto=5
i=0
soma=0
while(i<size(compra)):
	if(compra[i]>80):
		soma=soma+(compra[i]-desconto)
	soma=soma+compra[i]
	i=i+1
print(round(soma,2))
