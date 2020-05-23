qit = int(input("Qtd de tambaquis no tanque: "))
pct = int(input("% crescimento tambaqui: "))/100

qtv = 0

tbmes = qit
tA = 0
mes = 0

while tbmes > 0 and tbmes < 8000:
	qtv = int(input("Qtd tambaquis para venda: "))
	tA	 = tbmes + (tbmes*pct)
	tbmes = tA - (qtv)
		
	mes += 1	
	
	
	
if tbmes >= 8000:
	print("MAXIMO")
elif tbmes <= 0:
	print("ZERO")
	
print(mes)