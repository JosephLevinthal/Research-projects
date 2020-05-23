qit = int(input("Qtd de tambaquis no tanque: "))
pct = int(input("% crescimento tambaqui: "))/100
qtv = int(input("Qtd tambaquis para venda: "))

tbano = qit
tA = 0
ano = 0

while tbano > 0 and tbano < 12000:
	
	
	tA	 = tbano + (tbano*pct)
	tbano = tA - (qtv)
	
	ano += 1	
	
if tbano >= 1200:
	print("LIMITE")
elif tbano <= 0:
	print("EXTINCAO")
	
print(ano)