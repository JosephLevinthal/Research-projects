qtt = int(input("Quantidade de tambaqui:"))
pc = int(input("Percentual de crescimento:"))/100
qtv = int(input("Quantidade de tambaqui retirados para venda:"))

ano = 0

while(qtt > 0 and qtt < 12000):
	qtt = qtt*pc + qtt
	qtt = qtt - qtv
	ano = ano + 1
if(qtt < 0):
	print("EXTINCAO")
elif(qtt >= 12000):
	print("LIMITE")
print(ano)