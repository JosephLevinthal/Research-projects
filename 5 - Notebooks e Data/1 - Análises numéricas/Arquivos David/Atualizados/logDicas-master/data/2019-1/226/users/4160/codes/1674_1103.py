# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigiro.
x = float(input("Digite x: "))
a = float(input("Digite a: ")) 
b = float(input("Digite b: ")) 

if (b > a):
	if (x >= a) and (x <= b):
		print (x,"pertence ao intervalo", a ,",",b)
	else:
		print(x,"nao pertence ao intervalo", a , "," ,b)
else:
	print ("Entradas", a ,"e",b ,"invalidas")