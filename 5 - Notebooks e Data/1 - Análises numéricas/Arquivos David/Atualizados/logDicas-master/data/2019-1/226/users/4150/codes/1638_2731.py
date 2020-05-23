x = float(input("a: "))
y = float(input("b: "))
r = float(input("raio: "))

if (x > 0 and y>0 or x<0 and y>0 ):
	mensagem = "Superiores"
else:
	(x<0 and y<0 or x>0 and y<0)
	mensagem = "Inferiores"

print(mensagem)