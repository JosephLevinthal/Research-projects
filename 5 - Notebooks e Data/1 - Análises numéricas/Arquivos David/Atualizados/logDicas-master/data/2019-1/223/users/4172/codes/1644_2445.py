E = input("celsius/fahrenheit [C/F] : ")
T = float(input("temperatura: "))

C=5/9*(T-32)
F= (9/5 * T)+32

if E=="F":
	mensagem=(C)
else:
	mensagem=(F)
	
print(round(mensagem,2))