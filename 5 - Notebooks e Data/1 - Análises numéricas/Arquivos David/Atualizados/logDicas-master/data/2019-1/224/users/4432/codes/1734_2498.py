a=int(input("numero de habitntes na cidade A:  "))
b=int(input("numero de habitntes na cidade B:  "))
creA=float(input("Percentual de crescimento populacional da cidade A  "))
creB=float(input("Percentual de crescimento populacional da cidade B:  "))
cont=0
while(a<b):
	a=((a*creA)/100)+a
	b=((b*creB)/100)+b
	cont=cont+1
print(cont)
	
	