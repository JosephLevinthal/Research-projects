x = int(input("insira o numero:"))
y = int(input("insira o numero:"))
t = 0
d = 0
somax = 0


while(t <= x/2 ):
	t = t + 1
	if(x % t ==0):
		d = d + 1
		somax = somax + t
print(somax)
g = 0		
d1 = 0
somay = 0
while(g <= y/2):
	g = g + 1
	if(y % g == 0):
		d1 = d1 + 1
		somay = somay + g
print(somay)
if(somax == y and somay == x):
	print("AMIGOS")
else:
	print( "NAO AMIGOS")

