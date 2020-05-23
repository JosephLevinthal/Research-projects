# Ao testar sua solução, não se limite ao caso de exemplo.
he = float(input("numero de horas extras: "))
hf= float(input("numero de horas faltadas: "))
h= round(he - hf/4)
print(he, "extras e", hf,"de falta")
if h>400:
	print("R$ 500.0")
elif 0<=h<=400:
	print("R$ 100.0")