A=int(input("digite o numero de habitantes: "))
B=int(input("digite o numero de habitantes: "))
PA=float(input("digite o percentual: "))
PB=float(input("digite o percentual: "))
t=0
while (A<B):
	A=A+(A*PA/100)
	B=B+(B*PB/100)
	t=t+1
print(t)