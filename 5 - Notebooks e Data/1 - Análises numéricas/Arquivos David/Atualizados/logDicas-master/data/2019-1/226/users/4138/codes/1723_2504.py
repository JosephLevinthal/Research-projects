dia = 0
v = int(input("insira a quantidade inicial de virus:"))
l = int(input("insira a quantidade inicial de leucocitos:"))
pv = float(input("percentual de crescimento do virus:"))
pl = float(input("insira o percentual de crescimento de leucocitos:"))


while(l < 2*v):
	cv = (v * pv)/100
	cl = (l * pl)/100
	v = cv + v
	l = cl + l
	dia = dia + 1
print(dia)

	
