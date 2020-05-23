n=int(input("digite n: "))
cont=1 
div=-1
soma=0
while(cont<=n):
	cont=cont+1
	div=div+2
	soma=soma+((-1)**cont)*(4/div)
print(round(soma,8))