qv= int(input("qual a quantidade do virus?"))
ql= int(input("qual a quantidade inicial de leucocitos?"))
pv= int(input("qual o percentual de mp do virus?"))
pl= int(input("qual o percentual de mp dos leucocitos? "))
d=0

while(ql<=2*qv):
	qv= qv+ (pv/100)*qv
	ql= ql+(pl/100)*ql
	d= d+1
print(d)