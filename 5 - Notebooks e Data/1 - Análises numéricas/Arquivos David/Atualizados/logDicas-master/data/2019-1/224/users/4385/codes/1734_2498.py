A=int(input("digite o numero de habitantes: "))
B=int(input("digite o numero de habitantes: "))
P_A=float(input("digite o porcentual: "))
P_B=float(input("digite o porcentual: "))
t=0
while(A < B):
	A=A+(A*P_A/100)
	B=B+(B*P_B/100)
	t=t+1
print(t)