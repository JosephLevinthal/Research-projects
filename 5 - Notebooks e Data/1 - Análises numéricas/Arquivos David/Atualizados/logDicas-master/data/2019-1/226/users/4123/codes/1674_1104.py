# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input())
b = float(input())
c = float(input())
d = float(input())

print("Intervalo 1: ",a,", ",b)
print("Intervalo 2: ",c,", ",d)

if a>=b or c>=d:
	print("Entradas invalidas")
elif b<c:
	print("Nao ha intersecao")
else: 
	print("Ha intersecao")