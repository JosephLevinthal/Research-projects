from numpy import*
eusapia=array(eval(input("digite o numero:")))
barsanulfo=array(eval(input("digite o numero:")))
i=0
somae=0
somab=0
valore=0
valorb=0
while(i<size(eusapia)):
	if(eusapia[i]==33 and barsanulfo[i]==22):
		valore=1
		valorb=0
	elif(eusapia[i]==22 and barsanulfo[i]==11):
		valore=1
		valorb=0
	elif(eusapia[i]==11 and barsanulfo[i]==33):
		valore=1
		valorb=0
	elif(eusapia[i]==22 and barsanulfo[i]==33):
		valorb=1
		valore=0
	elif(eusapia[i]==11 and barsanulfo[i]==22):
		valore=0
		valorb=1
	elif(eusapia[i]==33 and barsanulfo[i]==11):
		valore=0
		valorb=1
	else:
		print("EMPATE")
		somae=somae+valorb
		somab=somab+valore
		i=i+1
print(size(e))
print("EUSAPIA")
print("BARSANULFO")