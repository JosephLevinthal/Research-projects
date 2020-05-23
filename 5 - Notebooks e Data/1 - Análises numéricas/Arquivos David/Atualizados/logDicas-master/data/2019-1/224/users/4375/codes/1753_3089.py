num=int(input("digite um numero:"))
cont=0
soma=0
while(num!=0):
	soma=soma+num
	num=int(input("digite um numero:"))
if(soma<0):
	print(soma)
	print("Esquerda")
if(soma>0):
	print(soma)
	print("Direita")
if(soma==0):
	print(soma)
	print("Inicial")