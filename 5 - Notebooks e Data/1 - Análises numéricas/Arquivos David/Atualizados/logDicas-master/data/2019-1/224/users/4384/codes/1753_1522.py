qi=int(input("valorem moedas: "))
dm=int(input("valor de despesas: "))
qm=int(input("moeda: "))
qr=int(input("roubadas: "))

acu=0
cont=1
while(qi==0):
	qtd=(((qi-dm)+qm)-qr)
	acu=qtd
	cont=cont+1
print(cont)