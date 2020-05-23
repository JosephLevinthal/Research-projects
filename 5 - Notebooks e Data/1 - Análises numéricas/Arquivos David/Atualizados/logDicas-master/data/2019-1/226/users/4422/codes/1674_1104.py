# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("Coordenada A: "))
b = float(input("Coordenada B: "))
c = float(input("Coordenada C: "))
d = float(input("Coordenada D: "))
print("Intervalo 1: ",a,",",b)
print("Intervalo 2: ",c,",",d)
if(b<=a) or (d<=c):
	print("Entradas invalidas")
elif(b<c):
	print("Nao ha intersecao")
else:
	print("Ha intersecao")
	