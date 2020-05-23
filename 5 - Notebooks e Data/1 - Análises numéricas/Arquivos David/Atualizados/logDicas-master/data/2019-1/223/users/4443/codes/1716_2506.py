#Entrada dos tambaquis, crescimento e venda:
t = int(input("Digite a quantidade inicial de tambaquis no tanque: "))
pc = float(input("Digite o percentual de crescimento: "))
qv = int(input("Digite a quantidade retirada para venda: "))		  
		  
anos = 0
while(0 < t < 12000):
	t = t + (t*pc/100)-qv
	anos = anos + 1
		
if (t <= 0):
	msg = "EXTINCAO"
elif (t >= 12000):
	msg = "LIMITE"
print(msg)
print(anos)		  
		  
		  
		  