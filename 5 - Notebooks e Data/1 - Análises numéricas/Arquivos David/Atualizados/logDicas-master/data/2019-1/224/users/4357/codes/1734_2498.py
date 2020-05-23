a=int(input("digite a cidade:"))
b=int(input("digite a cidade:"))
percentuala=float(input("digite o p:"))
percentualb=float(input("digite o p:"))
ano=0
while(a<b):
	a= a + a*(percentuala/100)
	b=b + b*(percentualb/100)
	ano= ano + 1
print(ano)
