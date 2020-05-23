var1 = float(input("Digite aqui o valor total: "))

tic = int(input("Digite aqui a quantidade de tickets: "))

var2 = float(input("Digite aqui o valor dos tickets: "))

oni = int(input("Digite aqui a quantidade de passes: "))

var3 = float(input("Digite aqui o valor "))

total = (tic * var2) + (oni * var3)

if (var1 >= total):
	msg = "SUFICIENTE"
else:
	msg = "INSUFICIENTE"
	
print(msg)