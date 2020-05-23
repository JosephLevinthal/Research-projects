a = int(input("digite o numero de habitantes da cidade A: "))
b = int(input("digite o numero de habitantes da cidade B: "))
pa = float(input("digite o percentual da cidade A: "))
pb = float(input("digite o percentual da cidade B: "))
c=0
while(a<b):
	pac=a*(pa/100)
	a=pac+a
	pbc=b*(pb/100)
	b=b+pbc
	c=c+1
print(c)