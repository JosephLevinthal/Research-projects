x=input("Digite C para Celsius ou F para Fanrenheit: ")
if(x.upper()=="C"):
	c=float(input("Digite a temperatura em celsius: "))
	c=c*1.8+32
	print(round(c,2))
else:
	f=float(input("Digite a temperatura em Fanrenheit:"))
	f=(f-32)/1.8
	print(round(f,2))
	