A = int(input("N de habitantes de A: "))
B = int(input("N de habitantes de B: "))
P_A = float(input("Percentual de crescimento A: "))
P_B = float(input("Percentual de crescimento B: "))

num_A = A
num_B = B

anos = 0

while(A < B):
	x = A * P_A / 100
	A = A + x
	y = B * P_B / 100
	B = B + y
	anos = anos + 1
	
print(anos)
	
	