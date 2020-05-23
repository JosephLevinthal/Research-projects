a = int(input("Quantidade inicial de pirarucu:"))
b = int(input("Percentual de crescimento:"))

x = b/100
t = 8000
mes = 0
	
while(a > 0) and (a <= t):
	c = int(input("Quantidade para venda:"))
	a = a +( a* x)
	a = a - c
	mes = mes + 1
if(a >= t):
	pa = "MAXIMO"
else:
	pa = "ZERO"

print(pa)
print(mes)