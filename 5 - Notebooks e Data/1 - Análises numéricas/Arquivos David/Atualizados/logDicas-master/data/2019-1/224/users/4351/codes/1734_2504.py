qntd1=int(input("qntd inicial de cop. virus: "))
qntd2=int(input("qntd inicial de leucocitos: "))
p1=float(input("percentual x diaria de virus: "))
p2=float(input("percentual x leucocitos: "))
tc1=p1/100 
tc2=p2/100
dias=0
while(2*qntd1>qntd2):
	qntd1=qntd1+qntd1*tc1
	qntd2=qntd2+qntd2*tc2
	dias=dias+1
print(dias)