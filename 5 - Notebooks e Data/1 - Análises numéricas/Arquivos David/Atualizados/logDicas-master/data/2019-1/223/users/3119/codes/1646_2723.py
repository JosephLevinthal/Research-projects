num1 = int(input("Digite o numero: ")) 
num2 = int(input("Digite o numero: ")) 
num3 = int(input("Digite o numero: ")) 
maximo = max(num1,num2,num3)

if(maximo == num1):
	msg = num1
if(maximo == num2):
	msg = num2
if(maximo == num3):
	msg = num3

print(msg)	