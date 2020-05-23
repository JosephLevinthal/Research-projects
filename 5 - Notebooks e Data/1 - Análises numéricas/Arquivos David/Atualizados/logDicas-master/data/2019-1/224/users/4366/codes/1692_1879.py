# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input("numero de horas extra: "))
y=float(input("numero de horas que o funcionario faltou: "))
h= x-(1/4*y)
print(x, "extras e", y, "de falta")
if(h>400):
	print("R$ 500.0")
elif(h<=400):
	print("R$ 100.0")