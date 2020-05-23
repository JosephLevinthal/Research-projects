num = int(input("Insira um numero de 3 digitos ou nao, tu que sabe:"))

n = num // 100
n1 = n*100
n2 = num - n1

if( num%n2 == 0):
	msg = "SIM"
else:
	msg = "NAO"
	
print(msg)	