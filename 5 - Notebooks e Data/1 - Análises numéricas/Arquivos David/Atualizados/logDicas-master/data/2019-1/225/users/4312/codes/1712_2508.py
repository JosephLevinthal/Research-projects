num = int(input("Digite um numero: "))

cont = 1

x =  3

while(cont < num):
	den = (cont*2) * (cont*2 +1) * (cont*2 + 2)
	x = x + (-1)**(cont + 1) * 4 / den
	cont = cont + 1
print(round(x, 8))
	
	
	
	
	
	
	
	
	