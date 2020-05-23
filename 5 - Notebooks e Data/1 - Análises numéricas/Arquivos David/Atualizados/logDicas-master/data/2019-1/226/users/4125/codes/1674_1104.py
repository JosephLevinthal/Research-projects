# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))
d = float(input("digite d: "))

print("Intervalo 1:",a,",",b)
print("Intervalo 2:",c,",",d)

if (b>a)and(d>c):
	if(a<=c)and(b>=c)or(b>=d)and(b>c)and(a<=c)and(a<=d):
		print("Ha intersecao")
	elif(a>c)and(a>d)or(b<c)and(b<d):
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")