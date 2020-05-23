qi = int(input("pirarucus no tanque: "))
pcm = float(input("percentual de crescimento mensal: "))

mes = 0 

while (qi > 0 and qi < 8000):	
	qr = int(input("pirarucus retirados mensalmente:"))
	qi = qi + ((qi * pcm)/100) - qr
	mes = mes + 1
	
if (qi <= 0):
	print("ZERO")
elif (qi >= 8000):
	print("MAXIMO")
	
print(mes)