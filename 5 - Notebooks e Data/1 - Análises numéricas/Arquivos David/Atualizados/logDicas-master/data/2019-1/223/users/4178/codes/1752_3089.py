n1 = int(input("Ponto inicial: "))
x = 0

while not (n1 == 0):
	x = x + n1
	n1 = int(input("Ponto inicial: "))
	
if (x < 0):
	print(x)
	print("Esquerda")
elif (x > 0)	:
	print(x)
	print("Direita")
else:
	print(x)
	print("Inicial")
	
	
	
