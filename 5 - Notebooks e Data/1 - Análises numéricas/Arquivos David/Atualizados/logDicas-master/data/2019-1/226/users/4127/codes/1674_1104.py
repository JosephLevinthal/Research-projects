# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a= float(input("qual seu ponto a? "))
b= float(input("qual seu ponto b? "))
c= float(input("qual seu ponto c? "))
d= float(input("qual seu ponto d? "))

print("Intervalo 1:", a,",", b)
print("Intervalo 2:", c, ",", d)

if(a>b or c>d):
	print("Entradas invalidas")
elif (c>b and c>a):
	print("Nao ha intersecao")
else:
	print("Ha intersecao")
	
