a= int(input("insira um numero de 3 dgts: "))

b = a//100
c = a%100

x = (a%c)

if x==0:
	print("SIM")
else:
	print("NAO")