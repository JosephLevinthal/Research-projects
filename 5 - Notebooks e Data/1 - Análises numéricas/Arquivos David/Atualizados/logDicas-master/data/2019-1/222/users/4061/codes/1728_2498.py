habA = int(input("digite habitantes A: "))
habB = int(input("digite habitantes B: "))
popA = float(input("digite percentual A: "))
popB = float(input("digite percentual B: "))

somaA = 0
somaB = 0
cont = 0
exit = 0
a = popA/100
b = popB/100

while(exit < 1):
	if (somaA > somaB):
		exit = 1
	somaA = habA * a
	somaB = habB * b
	cont = cont + 1

print(cont)
