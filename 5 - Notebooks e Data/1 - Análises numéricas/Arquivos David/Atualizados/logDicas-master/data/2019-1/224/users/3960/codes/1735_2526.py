n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

div1 = 0
div2 = 0
cont = 1

while(cont < n1 or cont < n2):
	if(n1 % cont == 0 and cont != n1):
		div1 = div1 + cont
	if(n2 % cont == 0 and cont != n2):
		div2 = div2 + cont
	cont = cont + 1
	
print(div1)
print(div2)

if(div1 == n2 and div2 == n1):
	print("AMIGOS")
else:
	print("NAO AMIGOS")