a = int(input("Quantidade inicial de tambaqui:"))
b = int(input("Percentual de crescimento:"))
c = int(input("Quantidade para venda:")) 

x = b/100
t = 12000 #tanqu
ano = 0
	
while(a > 0) and (a <= t):
	a = a +( a* x)
	a = a - c
	ano = ano + 1
if(a >= t):
	pa = "LIMITE"
else:
	pa = "EXTINCAO"
print(pa)
print(ano)