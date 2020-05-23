qi = int(input("quantidade inicial: "))
pc = int(input("percentual de acrescimo: "))
qv = int(input("quantidade para a venda: "))

cap = 8000
mes = 0

while (qi > 0) and (qi<cap):
	qi = qi +(qi * (pc/100))-qv
	mes = mes + 1
	
	if(qi>=cap):
		print("MAXIMO")
	elif(qi<=0):
		print("ZERO")
	else:
		qv = int(input("quantidade para a venda: "))
print(mes)
				