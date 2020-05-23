qp = int(input("Qtd. de pergaminhos: "))
qv = int(input("Qtd. de varinhas: "))
pp = float(input("P. de pergaminhos: "))
pv = float(input("P. de varinhas: "))
t = 0 #anos (contadora)
while (qp + qv <= 80000):
	qp = qp + (qp * pp/100)
	t = t + 1
	qv = qv + (qv * pv/100)
print(t)	

