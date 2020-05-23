#Entrada dos pirarucus, crescimento e venda:
p = int(input("Digite a quantidade inicial de pirarucus no tanque: "))
pc = float(input("Digite o percentual de crescimento: "))
		  
		  
meses = 0
while(0 < p < 8000):
	qv = int(input("Digite a quantidade retirada para venda: "))
	p = p + (p*pc/100)-qv
	meses = meses + 1
		
if (p <= 0):
	msg = "ZERO"
elif (p >= 8000):
	msg = "MAXIMO"
print(msg)
print(meses)		  