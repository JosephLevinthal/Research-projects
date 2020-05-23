A = int(input("digite o numero de habitantes da cidade A: "))
B = int(input("digite o numero de habitantes da cidade B: "))
a1 = float(input("digite o percentual de crescimento da cidade A: "))
b1 = float(input("digite o percentual de crescimento da cidade B: "))

a = a1/100
b = b1/100

t = 0

while A <= B:
	A1 = A*a
	A = A + A1
	B1 = B*b
	B = B + B1
	t = t+1
print(t)
	
	