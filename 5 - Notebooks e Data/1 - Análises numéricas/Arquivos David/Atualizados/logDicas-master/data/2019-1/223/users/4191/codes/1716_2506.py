#qp= quantidade de pexes acumulados
qip=int(input("Quuantidade inicial de peixe: "))
pc=int(input("Percentual de crescimento: "))
qv=int(input("Quantidades de peixe vendidos: "))

anos=0
qp=qip

while((qp>0)and(qp<12000)):
	qp=qp + qp*pc/100 - qv
	anos=anos+1
if(qp<=0):
	print('EXTINCAO')
elif(qp>=12000):
	print('LIMITE')

print(anos)	