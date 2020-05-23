n = int(input("numero: "))

qd=0
i = 1

while(i <= n):
	nu = n % i
	i = i + 1
	if(nu == 0):
		print(i-1)
		qd = qd + 1
	else:
		nu = nu

if(qd == 1):
	print(qd," divisor")
else:
	print(qd,"divisores")