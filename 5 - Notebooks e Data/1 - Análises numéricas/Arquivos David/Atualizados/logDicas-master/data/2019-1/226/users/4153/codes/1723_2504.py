# Quantidade inicial de copias de virus
w = int(input("Insira: "))
# Quantidade inicial de leucocitos
x = int(input("Insira: "))
# Percentual de multiplicacao
y = int(input("Insira: "))
# Percentual de multiplicacao
z = int(input("Insira: "))
d = 0

while(x < (2 * w)):
	r = (w * y)/100
	q = (x * z)/100
	w = w + r
	x = x + q
	d = d + 1
print(d)