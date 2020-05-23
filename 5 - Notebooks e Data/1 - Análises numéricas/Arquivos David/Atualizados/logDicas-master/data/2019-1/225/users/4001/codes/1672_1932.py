O1 = float(input("D. olhos 1: " ))
NQ1 = float(input("D. nariz e o queixo 1: "))
O2 = float(input("D. olhos 2: " ))
NQ2 = float(input("D. nariz e o queixo 2: "))
O3 = float(input("D. olhos 3: " ))
NQ3 = float(input("D. nariz e o queixo 3: "))
# Razoes
I1 = O1/NQ1
I2 = O2/NQ2
I3 = O3/NQ3
if (abs(I1 - I2) <= 0.01 ):
	print(1, " e ", 2)
elif (abs(I1 - I3) <= 0.01):
	print(1, " e ", 3)
elif (abs(I2 - I3) <= 0.01):
	print(2, " e ", 3)
