num1 = int(input("Digite o numero: ")) 
num2 = int(input("Digite o numero: ")) 
num3 = int(input("Digite o numero: ")) 
minimo = min(num1,num2,num3)
maximo = max(num1,num2,num3)
medio = (num1 + num2 + num3) - minimo - maximo

if(medio == num1):
	msg = num1
if(medio == num2):
	msg = num2
if(medio == num3):
	msg = num3

print(msg)	