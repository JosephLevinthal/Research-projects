qinicial= int(input("quantidade inicial: "))
perc= float(input("percentual de crescimento: "))
perc= perc/100
t=0
while(0 < qinicial <= 8000):
	quant= int(input("nova quantidade: "))
	qinicial= (qinicial + qinicial * perc) - quant
	t= t + 1
if(qinicial<=0):
	print("ZERO")
	print(t)
if(qinicial>=8000):
	print("MAXIMO")
	print(t)