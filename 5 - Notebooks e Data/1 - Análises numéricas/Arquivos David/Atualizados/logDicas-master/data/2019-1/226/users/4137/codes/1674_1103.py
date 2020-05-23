# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("insira o valor de x:"))
a = float(input("insira o valor de a:"))
b = float(input("insira o valor de b:"))

if(b <= a):
	print("Entradas" , a ,"e", b , "invalidas")
elif(x <= b and x >= a):
	print(x , "pertence ao intervalo" , a ,",", b)
elif(x > b or x < a):
	print(x , "nao pertence ao intervalo", a ,",", b)
