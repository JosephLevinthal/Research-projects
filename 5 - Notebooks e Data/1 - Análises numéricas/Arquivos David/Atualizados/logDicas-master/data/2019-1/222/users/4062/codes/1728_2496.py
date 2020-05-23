soma=0
cont=0
num=int(input("numero: "))
while(num!=-1):
	soma=soma+num
	cont=cont+1
	num=int(input("numero: "))
if(cont>0):
	print(soma)
