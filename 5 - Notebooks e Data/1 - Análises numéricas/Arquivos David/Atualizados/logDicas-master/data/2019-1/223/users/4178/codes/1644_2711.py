var1 = int(input("Valor disponivel: "))
var2 = int(input("Quantidades de tickets do RU: "))
var3 = float(input("Valor dos tickets: "))
var4 = int(input("Quantidades de passe de onibus: "))
var5 = float(input("Valor das passgens: "))

total = (var2*var3)+(var4*var5)

if total < var1 :
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")