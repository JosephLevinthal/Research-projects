qp= int(input("insira a quantidade inicial de pirarucus no tanque: "))
pc= int(input("insira o percentul de cresciment mensal de pirarucus: "))/100
v=0
t=0
while qp>0 and qp<=8000:
	qtv=int(input("insira a quantidade de pirarucus retiradas todos os meses para venda: "))
	v=(qp*pc)-qtv
	qp=qp+v
	t=t+1
if qp<=0:
	print("ZERO")
elif qp>=8000:                    
	print("MAXIMO")
print(t)