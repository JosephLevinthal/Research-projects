# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a= float(input("pontoA: "))
b= float(input("pontoB: "))
c= float(input("pontoC: "))
d= float(input("pontoD"))

print("Intervalo:", a, ",", b)
print("Intervalo:", c, ",", d)

if (b < a or d < c):
	print("Entradas invalidas")
elif(b >= c or b>= d):
	print("Ha intersecao")
else:
	print("Nao ha intersecao")