# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
x = float(input("qual teu cunsumu mouusa: "))
tipo = input("tipo da sua instalacion sinhor")
print("Entradas:" , x ,"kWh" ,"e", "tipo" , tipo)
if (x > 0) or (tipo != "R" or "I" or "C"):
	if (x <= 1000) and (tipo == "C") :
		x = (x * 0.55)
		print("Valor total: R$", round(x,2))
