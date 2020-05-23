a = float(input("Qual valor que voce tem disponivel? "))
b = int(input("Qual a quantidade de tickets do RU? "))
c = float(input("Qual o valor do tickets? "))
d = int(input("Qual a quantidade de passes? "))
e = float(input("Qual o valor dos passes? "))
valor = a - (b * c)
valor1 = valor - (d * e)
if (valor1 >= 0) : 
	print("SUFICIENTE")
else : 
	print ("INSUFICIENTE")