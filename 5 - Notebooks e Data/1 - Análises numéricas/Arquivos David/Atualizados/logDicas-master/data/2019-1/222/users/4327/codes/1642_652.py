a=int(input("digite um numero de tres digitos: "))

b=a//100
res=a%b

if(res == 0):
	print("SIM")
else:
	print("NAO")