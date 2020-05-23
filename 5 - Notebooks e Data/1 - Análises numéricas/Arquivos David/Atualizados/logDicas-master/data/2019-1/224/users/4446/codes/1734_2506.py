qinicial= int(input("quantidade inicial: "))
perc= float(input("percentual de crescimento: "))
quant= int(input("quantidade de pirarucus retirados: "))
perc= perc/100
t=0
while(0<=qinicial<=12000):
	qinicial= (qinicial + qinicial * perc) - quant
	t= t +1
if(qinicial<=0):
	print("EXTINCAO")
	print(t)
if(qinicial>= 12000):
	print("LIMITE")
	print(t)