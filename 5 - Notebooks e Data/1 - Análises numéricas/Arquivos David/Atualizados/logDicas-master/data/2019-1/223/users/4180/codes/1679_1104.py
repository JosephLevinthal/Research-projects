# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a = float(input("digite um valor para a:"))
b = float(input("digite um valor para b:"))
c = float(input("digite um valor para c:"))
d = float(input("digite um valor para d:"))

if((a > b) or (c > d)):
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Entradas invalidas")
	
elif(c <= b and b <= d) or(a <= c and d <= b) or (c <= a and b <= d) or (c <= a and a<= d):
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Ha intersecao")
	
elif(((b > a) and (b < c) and (b < d)) or ((d > c) and (d < a) and (d < b))):
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Nao ha intersecao")