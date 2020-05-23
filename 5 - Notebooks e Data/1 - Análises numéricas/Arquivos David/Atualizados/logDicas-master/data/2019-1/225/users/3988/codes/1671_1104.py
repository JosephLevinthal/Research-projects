# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
print("Intervalo 1:", a,",", b)
print("Intervalo 2:", c,",", d)
if((b>a) and (d>c)):
   if((c >= a) and (c <= b) or (d >= a) and (d <= b)):
	   print("Ha intersecao")
   else:
	   print("Nao ha intersecao")
else:
	print("Entradas invalidas")