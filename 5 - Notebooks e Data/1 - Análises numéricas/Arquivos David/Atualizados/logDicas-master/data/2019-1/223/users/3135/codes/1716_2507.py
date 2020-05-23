qin=int(input("Insira a quantidade inicial:"))
p=float(input("Insira a quantidade de crescimento:"))
cont=0
res=qin
while(res>0 and res<8000):
	venda=int(input("Insira o valor de cada mes:"))
	if(cont==0):
		res = qin*(p/100) + qin-venda
	else:
		res = qin*(p/100) + res-venda
	cont+=1
if(res<0):
	print("ZERO".upper())
elif(res>=8000):
	print("MAXIMO".upper())
print(cont)