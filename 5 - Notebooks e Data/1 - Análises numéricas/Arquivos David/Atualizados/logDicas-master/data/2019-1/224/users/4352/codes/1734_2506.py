qit=int(input("quantidade de inicial: "))
pc=float(input("percentual de crescimento: "))
qtr=int(input("tambaquis retirados: "))
a=0
while(0<qit<=12000):
	r=qit*(pc/100)
	qit=qit+r-qtr
	a=a+1
if(qit<=0):
	print("EXTINCAO")
	print(a)
elif(qit>=12000):
	print("LIMITE")
	print(a)