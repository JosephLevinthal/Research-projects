# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
c = float(input("Digite um numero: "))
d = float(input("Digite um numero: "))

print("Intervalo 1: {} , {}".format(a,b))
print("Intervalo 2: {} , {}".format(c,d))

if not(b > a) and (d > c):
	print("Entradas invalidas")
	
elif ((c > a) and (c < b))or ((d < b) and (d > a)):
	print("Ha intersecao")
elif (c > b or d < a):
	print("Nao ha intersecao")