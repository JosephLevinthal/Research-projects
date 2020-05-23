# Leitura dos numeros reais
x = float(input("Digite um valor para x: "))
a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))

# Verificacao se x pertence ao intervalo
if(b <= a):
	print("Entradas", a, "e", b, "invalidas")
elif(a <= x) and (x <= b):
	print(x, "pertence ao intervalo ", a, ",", b)
else:
	print(x, "nao pertence ao intervalo ", a, ",", b)
	
	