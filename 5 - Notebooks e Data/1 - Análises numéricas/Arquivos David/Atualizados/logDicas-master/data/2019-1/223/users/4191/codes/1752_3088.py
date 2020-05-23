num=int(input("numero inteiro:"))
cont=0
impar=0
par=0
while(num!=0):
	cont=cont+1
	if((num%2==0)and(num!=0)):
		par=par+1
		
	else:
		impar=impar+1
	num=int(input("numero inteiro: "))	
result=par/cont*100
resultado=impar/cont*100
print(round(result, 2))
print(round(resultado, 2))
		