x = float(input("Digite a coordenada x"))
y = float(input("Digite a coordenada y"))
r = float(input("Digite o valor: "))

if(x > 0 and y > 0 or x < 0 and y > 0):
	print("Superiores")
if(x < 0 and y < 0 or x > 0 and y < 0):
	print("Inferiores")