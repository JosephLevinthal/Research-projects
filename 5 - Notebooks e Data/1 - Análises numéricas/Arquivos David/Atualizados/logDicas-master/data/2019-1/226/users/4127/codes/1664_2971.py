j= float(input("qual a taxa de juros? "))
vl= float(input("qual o valor do apartamento? "))
t= 36
q0= 1500
qf= q0*(1+j)**36
if (qf>=vl):
	print(round(qf,2),"Sim")
else:
	print(round(qf,2),"Nao")