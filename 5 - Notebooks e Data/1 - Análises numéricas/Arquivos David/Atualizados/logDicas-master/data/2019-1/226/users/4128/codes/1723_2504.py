a = int(input("Quantidade inicial de copias virus:"))
b = int(input("Quantidade inicial de leucocitos:"))
c = int(input("Percentual do virus:")) 
d = int(input("Percentual do leucocitos:")) 

x = c/100
y = d/100
dia = 0 

while (a*2 > b):
	a = a + (a * x)
	b = b + (b * y) 
	dia = dia + 1
print(dia)