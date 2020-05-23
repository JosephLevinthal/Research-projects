t = int(input("Quantidade inicial de tambaquis: "))
pc = int(input("Percentual de crescimento: ")) / 100
qr = int(input("Quantia retirada do tanque: "))

a = 0

while(t > 0 and t < 12000):
	t = t + t * pc - qr
	a = a + 1
if(t <= 0):
	print("EXTINCAO")
else:
	print("LIMITE")
print(a)