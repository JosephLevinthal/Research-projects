A = int(input("no. de habitantes A: "))
B = int(input("no. de habitantes B: "))
a1 = float(input("percentual de habitantes a: ")) 
b1 = float(input("percentual de habitantes b: "))

va = A
vb = B
n = 0

while(A<B and a1>b1):
	va = A * (a1/100)
	vb = B * (b1/100)
	n = n+1
	print(n)

		