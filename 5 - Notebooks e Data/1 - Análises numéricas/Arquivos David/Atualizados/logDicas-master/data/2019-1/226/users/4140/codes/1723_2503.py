#mesmo sistema de oscilação de mais e menos 
#soma em numeros impares no denominador
n=int(input())
resultado=0
i=0
while(i<n):
	soma=(((-1)**i)*4)/(1+2*i)
	resultado=resultado+soma
	i=i+1
print(round(resultado,8))
