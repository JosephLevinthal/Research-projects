# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a=float(input("numero a: "))
b=float(input("numero b: "))
c=float(input("numero c: "))
d=float(input("numero d: "))
print("Intervalo 1:", a,",",b)
print("Intervalo 2:", c,",",d)
if((b<=a)or(d<=c)):
	print("Entradas invalidas")
