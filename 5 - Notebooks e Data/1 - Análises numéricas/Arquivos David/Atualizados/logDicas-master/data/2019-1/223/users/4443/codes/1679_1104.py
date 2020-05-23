# Leitura dos intervalos
a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))
d = float(input("Digite um valor para d: "))

#Verificacao dos intervalos
if(a>b) or (c>d):
	print("Intervalo 1:", a,",", b)
	print("Intervalo 2:", c,",", d)
	print("Entradas invalidas")

elif(c >= a) and (c <= b): 
	print("Intervalo 1:", a,",", b)
	print("Intervalo 2:", c,",", d)
	print("Ha intersecao")

elif(a >= c) and (a <= d):
	print("Intervalo 1:", a,",", b)
	print("Intervalo 2:", c,",", d)
	print("Ha intersecao")

elif(d >= a) and (d <= c):
	print("Intervalo 1:", a,",", b)
	print("Intervalo 2:", c,",", d)
	print("Ha intersecao")

elif(b <= d) and (b >= c):
	print("Intervalo 1:", a,",", b)
	print("Intervalo 2:", c,",", d)
	print("Ha intersecao")

elif(c>a) or (a>d):
	print("Intervalo 1:", a,",", b)
	print("Intervalo 2:", c,",", d)
	print("Nao ha intersecao")

