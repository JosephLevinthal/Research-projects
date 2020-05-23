x = int(input("Digite um numero inteiro: "))
z = int(input("Digite um numero inteiro: "))
y = 0
a = 0
totalx = 0
totalz = 0
while(y < x - 1):
	y = y + 1
	if(x % y == 0):
		totalx = totalx + y
while(y < z - 1):
	a = a + 1
	if(z % a == 0):
		totalz = totalz + a
print(totalx)
print(totalz)
if(totalx == z):
	print("AMIGOS")
else:
	print("NAO AMIGOS")