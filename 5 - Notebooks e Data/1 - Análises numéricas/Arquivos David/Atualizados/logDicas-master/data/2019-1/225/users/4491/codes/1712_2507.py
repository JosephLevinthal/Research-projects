qtd = int(input("qtd inicial de pirarucu: "))
per1 = float(input("percentual de crescimento: "))

t = 0
while(qtd < 8000) and (qtd > 0):
	qt = int(input("a cada mes: "))
	qtd = qtd + ((qtd * per1) / 100) - qt
	t = t + 1
	
if(qtd >= 8000):
	print("MAXIMO")
elif(qtd <= 0):
	print("ZERO")
	
print(t)