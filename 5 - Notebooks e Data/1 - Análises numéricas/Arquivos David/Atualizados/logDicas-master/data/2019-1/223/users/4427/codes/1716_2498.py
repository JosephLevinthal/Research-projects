a = int(input("Numero de habitantes A: "))
b = int(input("Numero de habitante B: "))
x = float(input("Percentual de crescimento A: "))
y = float(input("Percentual de crescimento B: "))

c = 0

while (a<b):
	a = a+(a*(x/100))
	b = b+(b*(y/100))
	c += 1

print(c)