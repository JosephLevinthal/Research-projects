qntd1=int(input("quantidade inicial de pergaminhos: "))
qntd2=int(input("quantidade de varinhas guardadas: "))
p1=float(input("percentual de crescimento dos pergaminhos: "))
p2=float(input("percentual de crescimento das varinhas:"))
tc1=p1/100
tc2=p2/100
anos=0
while(0<iten>=80000):
	qntd1=qntd1+qntd1*tc1
	qntd2=qntd2+qntd2*tc2
	anos=anos+1
print(anos)
