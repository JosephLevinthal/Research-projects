# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a = float(input("digite numero a: "))
b = float(input("digite numero b: "))
c = float(input("digite numero c: "))
d = float(input("digite numero d: "))

print("Intervalo: ",a ",", b)
print("Intervalo: ",c ",", d)

if(b < a and d < c):
	print("Entradas invalidas")
elif(b > a and d > c):
	print(" Nao ha intersecao")
else:
	print("Ha intersecao")
