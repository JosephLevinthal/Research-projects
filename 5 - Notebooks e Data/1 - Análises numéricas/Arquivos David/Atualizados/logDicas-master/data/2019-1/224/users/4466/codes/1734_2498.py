A = int(input("digite o numero de habitantes: "))
B = int(input("digite o numero de habitantes: "))
p_A = float(input("digite o percentual: "))
p_B = float(input("digite o percentual: "))
t = 0
while(A < B):
	A = A + (A * p_A/100)
	B = B + (B * p_B/100)
	t = t+1
print(t)