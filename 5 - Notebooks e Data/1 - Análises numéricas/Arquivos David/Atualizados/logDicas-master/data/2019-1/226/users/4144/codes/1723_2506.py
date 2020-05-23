a = int(input("qtd inicial de tambaquis: "))
b = float(input("percentual de crescimento anual: "))
c = int(input("qtd de tambaquis para venda: "))
i = 0
while(a>0 and a<12000):
	txp = (a*b)/100
	a= a+txp-c
	i = i+1
if(a<0):
	print("EXTINCAO")
else:
	print("LIMITE")
print(i)