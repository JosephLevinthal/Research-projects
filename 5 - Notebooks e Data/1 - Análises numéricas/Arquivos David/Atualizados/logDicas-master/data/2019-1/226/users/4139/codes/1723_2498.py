A = int(input("numero de habitantes: "))
B = int(input("numero de habitantes: "))
a = float(input("percentual de crecimento de cidade A: "))
b = float(input("percentua de crescimento de cidade B: "))

pa = a / 100
pb = b / 100

ano = 0

while(A < B):
	A = A + (A * pa)
	B = B + (B * pb)
	ano = ano + 1

print(ano)