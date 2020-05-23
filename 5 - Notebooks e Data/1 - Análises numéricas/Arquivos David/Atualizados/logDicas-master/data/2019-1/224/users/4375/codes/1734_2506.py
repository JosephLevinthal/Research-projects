qnt1=int(input("quantidade inicial de tambaquis: "))
pc=int(input("percentual de crescimento: "))
bye=int(input("quantidade de tambaquis retirados para money: "))
por=pc/100
anos=0
while(0<qnt1<=12000):
	qnt1=(qnt1+qnt1*por)-bye
	anos=anos+1
if(qnt1<=0):
		print("EXTINCAO")
		print(anos)
if(qnt1>=12000):
		print("LIMITE")
		print(anos)
