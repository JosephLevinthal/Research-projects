escala=input("digite qual escala de convecao(c=celsius ou f=farenheit):  ")
temp=float(input("digite o valor da temperatura:"))

if(escala.upper()=="F"):
	c=(temp-32)*(5/9)
	print (round(c,2))
else:
	f=(temp/(5/9))+32
	print (round(f,2))