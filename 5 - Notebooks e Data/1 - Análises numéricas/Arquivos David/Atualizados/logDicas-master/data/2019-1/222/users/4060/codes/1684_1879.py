# Ao testar sua solução, não se limite ao caso de exemplo.
e=float(input("numero de horas extra: "))
f=float(input("numero de horas faltadas: "))
h=e-(1/4*f)
print(e, "extras e", f ,"de falta")
if(h>400):
	print("R$ 500.0")
elif(h<=400):
	print("R$ 100.0")
