q_inicial=int(input("quantidade inicial: "))
perc=float(input("percentual de crescimento: "))
perc=perc/100
t=0
while(0<q_inicial<=8000):
	quant=int(input("nova quantidade: "))
	q_inicial=(q_inicial+q_inicial*perc)-quant
	t=t+1
if (q_inicial<=0):
	print("ZERO")
	print(t)
if(q_inicial>=8000):
	print("MAXIMO")
	print(t)