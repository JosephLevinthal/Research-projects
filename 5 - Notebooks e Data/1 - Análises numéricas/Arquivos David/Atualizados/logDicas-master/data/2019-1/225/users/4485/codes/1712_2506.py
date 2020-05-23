q1=int(input("quantidade inicial de tamabaqui: "))
p1=float(input("percentual de crescimento: "))
q2=int(input("tambaqui para venda: "))
a=q1
t=0
while (a<12000) and (a>0) and (p1>0) and (q2>0):
	t=t+1
	a=a+(a*(p1/100))
	a=a-q2
if(a>=12000):
	print("LIMITE")
	print(t)
else:
	print("EXTINCAO")
	print(t)