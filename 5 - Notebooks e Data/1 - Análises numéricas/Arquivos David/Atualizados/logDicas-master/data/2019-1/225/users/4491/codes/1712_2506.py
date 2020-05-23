qtd = int(input("qtd de tambaqui: "))
per1 = float(input("percentual de crescimento: "))
per2 = int(input("qtd de venda: "))

t = 0

while(qtd < 12000) and (qtd > 0):
	qtd = qtd + ((qtd * per1 / 100)) - per2
	t = t + 1

if(qtd >= 12000):
	print("LIMITE")
elif(qtd <= 0):
	print("EXTINCAO")
	
print(t)