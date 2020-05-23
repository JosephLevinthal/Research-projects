inicial=int(input("digite a quantidade inicial de tambaquis:"))
percentual=int(input("digite o percentual de crescimento anual:"))
venda=int(input("digite  a quantidade de tambaquis retirados todos os anos para venda:"))
percentual=percentual/100
t=0
while(0<=inicial<=12000):
	inicial=(inicial+inicial*percentual)-venda
	t=t+1
if(inicial<=0):
	print("EXTINCAO")
	print(t)
if(inicial>=12000):
	print("LIMITE")
	print(t)
		