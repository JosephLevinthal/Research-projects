# Ao testar sua solução, não se limite ao caso de exemplo.
e = float(input("horas extras: "))
f = float(input("horas que faltou: "))

print(e," extras e ",f," de faltas ")
h = e - (1/4 * f)

if(h<=400):
	g=100.0
	print("R$",round(g,2))
elif(h>400):
	g=500.0
	print("R$",round(g,2))