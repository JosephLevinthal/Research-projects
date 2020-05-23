# Ao testar sua solução, não se limite ao caso de exemplo.
nhe= float(input("insira o numero de horas extras: "))
nhef= float(input("insira o numero de horas que o funcionario faltou: "))
h=(nhe)-(1/4)*nhef
if h>400:
	g=500.00
elif h<=400:
	g=100.00
print(nhe,"extras e",nhef,"de falta")
print("R$",round(g,2))
