a = int(input("Digite habitantes da cidade a:"))
b = int(input("Digite habitantes da cidade b:"))
a1 = float(input("Crescimento de a:"))
b1 = float(input("Crescimento de b:"))
percA = a1/100 #PERCENTUAL DE CRESCIMENTO DE A
percB = b1/100  #PERCENTUAL DE CRESCIMENTO DE B

#VARIAVEL CONTADORA
ano = 0

while (a<b):
	a= a+(a*percA)
	b = b+(b*percB)
	ano = ano +1
print(ano)