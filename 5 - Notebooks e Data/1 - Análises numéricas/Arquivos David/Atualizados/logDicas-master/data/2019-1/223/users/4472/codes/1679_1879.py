horasExtras = float(input("Horas extras: "))
horasFaltas = float(input("Horas que funcionario faltou: "))
indiceH = (horasExtras) - 1/4 * (horasFaltas)

if indiceH > 400:
	gratificacao = 500.00
elif indiceH <= 400:
	gratificacao = 100.00
#else:
#	gratificacao = 100.00

print (horasExtras,"extras e",horasFaltas,"de falta")
print ("R$",round(gratificacao,2))
