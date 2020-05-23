# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
c = float(input("Digite um numero: "))
d = float(input("Digite um numero: "))

print( "Intervalo 1:", a ,",", b)
print( "Intervalo 2:", c ,",", d)

if (b > a) and (d > c):
	if(( (c < a ) and ( d < a)) or (( d > b) and (c > b) )):
		print("Nao ha intersecao")
	else:
		print("Ha intersecao")
else:
	print("Entradas invalidas")
