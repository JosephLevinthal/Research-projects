# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))
d = float(input("digite d: "))

if (a < b and d > c):
	print("Intervalo 1",a, ",", b)
	print("Intervalo 2",c, ",", d)
		
elif(a <= d):
	 print("Ha intersecao")
		
elif(a <= c):
	 print("Ha intersecao")
		
elif(b <= c):
	 print("Ha intersecao")
		
elif(d >= b):
	 print("Ha intersecao")
		
elif(not(a >= d and a >= d and b <= c and d <= b and d >= b)):
	      print("Nao ha intersecao")
		
else:
	 print("Entradas invalidas")