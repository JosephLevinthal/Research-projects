sucos=int(input("Quantos sucos desejam?"))
s=int(input("E quantos salgados?"))
din=float(input("Valor em dinheiro:"))
x=((sucos*3)+(s*3.5))
print(round(x,1))
if(x>din):
	falta=x-din
	print("Nao")
else:
	print("Sim")