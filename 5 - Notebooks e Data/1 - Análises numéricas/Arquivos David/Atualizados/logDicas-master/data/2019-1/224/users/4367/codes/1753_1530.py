qpi=int(input("escreva a quantidade de pergaminhos: "))
qvi=int(input("quantidade de varinhas: "))
pp=float(input("escreva a quantidade do percentual de pergaminhos: "))
pv=float(input("percentual de varinhas: "))
c=0
while(qpi+qvi<80000):
	ppp=qpi*(pp/100)
	qpi=qpi+ppp
	pvv=qvi*(pv/100)
	qvi=qvi+pvv
	c=c+1
print(c)