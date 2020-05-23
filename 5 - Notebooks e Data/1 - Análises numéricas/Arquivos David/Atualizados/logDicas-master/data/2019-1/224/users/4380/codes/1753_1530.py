p=int(input("qtd inicial de pergaminhos: "))
v=int(input("qtd inicial de varinhas magicas: "))
pp=float(input("percentual dos pergaminhos: "))
pv=float(input("percentual das varinhas magicas: "))
lim=80000
t=0
while (p+v<lim):
	p=p+(p*pp/100)
	v=v+(v*pv/100)
	t=t+1
print(t)