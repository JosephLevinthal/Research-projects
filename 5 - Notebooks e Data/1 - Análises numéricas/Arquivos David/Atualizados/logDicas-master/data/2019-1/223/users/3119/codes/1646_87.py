num1 = int(input("Digite o numero: ")) 
num2 = int(input("Digite o numero: ")) 
num3 = int(input("Digite o numero: ")) 
minimo = min(num1,num2,num3)

if(minimo == num1):
	msg = num1
if(minimo == num2):
	msg = num2
if(minimo == num3):
	msg = num3

print(msg)	