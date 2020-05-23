n = int(input("Digite o numero: "))

cont = 0
par = 0
impar = 1
tp = 0
ti = 0

while(n != 0):
	if((n % 2) == 0):
		tp = n + ((cont * par) / 100)
	else:
		ti = n + ((cont * impar) / 100)
			
	tp = par + 1
	ti = impar + 2
	cont = cont + 1
	
	n = int(input("Digite o numero: "))

print(tp)
print(ti)