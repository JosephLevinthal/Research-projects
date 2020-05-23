n = int(input("Insira o numero: "))
x = n % 100
y = n % x

if(n % x == 0):
	msg = "SIM"
else:
	msg = "NAO"

print(msg)