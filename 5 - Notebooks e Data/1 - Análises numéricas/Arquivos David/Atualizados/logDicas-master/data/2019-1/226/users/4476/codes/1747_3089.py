m1 = int(input("digite o numero: "))

i = 0

while (m1!=0):
	i = i + m1
	m1 = int(input("digite o numero: "))
if (i>0):
	print(i)
	print("Direita")
if (i<0):
	print(i)
	print("Esquerda")
if (i==0):
	print(i)
	print("Inicial")
