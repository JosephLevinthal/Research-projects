# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("Digite a coordenada x"))
y = float(input("Digite a coordenada y"))
if(x > 0 and y > 0 or x < 0 and y > 0):
	print("Superiores")
if(x < 0 and y < 0 or x > 0 and y < 0):
	print("Inferiores")