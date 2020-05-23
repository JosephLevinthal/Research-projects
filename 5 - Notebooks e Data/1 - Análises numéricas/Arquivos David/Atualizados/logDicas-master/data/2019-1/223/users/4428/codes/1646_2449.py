a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
d = float(input("Valor de d: "))
e = float(input("Valor de e: "))
f = float(input("Valor de f: "))

x = int(c*e - b*f)/(a*e - b*d)
y = int(a*f - c*d)/(a*e - b*d)

if(x !=0, y!=0):
	
	print(x)
	print(y)

else:
	mensagem = "Nao tem solucao"
	print(mensagem)