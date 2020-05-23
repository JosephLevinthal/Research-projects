a = int(input("num apostado c dois digitos: "))
b = int(input("num sorteado pela loteria: "))
dig1a= a//10
dig2a= a%10
dig1b= b//10
dig2b= b%10
if(a==b):
	print("Ganhou R$ 100.000,00")
elif(dig1a==dig2b and dig2a==dig1b):
	print("Ganhou R$ 50.000,00")
elif(dig1a==dig1b or dig2a==dig1b or dig1a==dig2b or dig2a=dig2b):
	print("Ganhou R$ 1.000,00")
else:
	print("perdeu")
	
