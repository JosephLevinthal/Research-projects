# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Insira o numero: "))
a = float(input("Insira o numero: "))
b = float(input("Insira o numero: "))

if(b <= a):
	print("Entradas ", a,"e", b,"invalidas")
elif(a <= x <= b):
	print(x," pertence ao intervalo", a,",", b)
elif((x < a) or (x > b)):
	print(x,"nao pertence ao intervalo", a, "," , b)