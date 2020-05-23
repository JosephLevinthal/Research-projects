x = int(input())
y = int(input())

contadorx = x - 1
contadory = y - 1

somax = 0
somay = 0

while(contadorx > 0):
	if(x % contadorx == 0):
		somax = somax + contadorx
		
	contadorx = contadorx - 1

while(contadory > 0):
	if(y % contadory == 0):
		somay = somay + contadory
		
	contadory = contadory - 1

print(somax)
print(somay)

if(somax == y and somay == x):
	print("AMIGOS")
else:
	print("NAO AMIGOS")