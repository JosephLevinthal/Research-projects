q1 = int(input("quantidade inicial de tambaquis:"))
pn = int(input("percentual de crescimento anual:"))
qv = int(input("quantidade de tambaquins pra venda:"))
a = q1
cont = 0

while(a < 12000 and a > 0):
	a = a + (a * pn / 100)
	a = a - qv
	cont = cont + 1
if(a >= 12000):
	print("LIMITE")
	print(cont)
else:
	print("EXTINCAO")
	print(cont)