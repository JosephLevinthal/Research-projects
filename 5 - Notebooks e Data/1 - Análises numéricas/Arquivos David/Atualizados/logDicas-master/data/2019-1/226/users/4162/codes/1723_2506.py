qt= int(input("insira a quantidade inicial de tambaquis no tanque: "))
pc= int(input("insira o percentul de crescimento anual de tambaquis: "))/100
qtv=int(input("insira a quantidade de tambaquis retiradas todos os anos para venda: "))
ta=0
t=0
while qt>0 and qt<=12000:
	qt=qt+ta
	t=t+1
	ta=((qt*pc)-qtv)
if qt<=0:
	print("EXTINCAO")
elif qt>=12000:
	print("LIMITE")
print(t-1)