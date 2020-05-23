a = int(input("Informe um numero qualquer para 'A': \n"))
b = int(input("Informe um numero qualquer para 'B': \n"))

cont = 1
x = 0

cont2 = 1
x2 = 0

while(cont<a):
	if(a%cont==0):
		x = x + cont

	cont = cont + 1
print(x)
while(cont2<b):
	if(b%cont2==0):
		x2 = x2 + cont2
	
	cont2 = cont2 + 1
print(x2)	
if (x2==a)and(x==b):
	print("AMIGOS")
else:
	print("NAO AMIGOS")