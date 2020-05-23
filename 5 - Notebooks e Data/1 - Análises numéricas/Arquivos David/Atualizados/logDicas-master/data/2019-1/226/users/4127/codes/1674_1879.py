# Ao testar sua solução, não se limite ao caso de exemplo.
x= float(input("qual o numero de horas extras: "))
y= float(input("qual o numero de horas faltadas: "))

h= round(x - y/4)
print(x,"extras e", y,"de falta")
if (h>400):
	print("R$ 500.0")
elif (0<=h<=400):
	print("R$ 100.0")