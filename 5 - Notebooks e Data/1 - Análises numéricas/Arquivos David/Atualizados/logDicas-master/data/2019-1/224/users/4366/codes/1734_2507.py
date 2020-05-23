quant=int(input("digite a quantidade inicial: "))
cresc=int(input("digite o percentual de crescimento:"))
por=cresc/100
meses=0
while(0<quant<=8000):
	venda=int(input("digite a quantidade de vendas:"))
	quant=(quant+quant*por)-venda
	meses=meses+1
if(quant<=0):
	print("ZERO")
	print(meses)
if(quant>=8000):
	print("MAXIMO")
	print(meses)	