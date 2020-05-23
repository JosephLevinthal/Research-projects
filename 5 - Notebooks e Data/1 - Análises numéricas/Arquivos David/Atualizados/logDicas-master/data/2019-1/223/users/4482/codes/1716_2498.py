a = int(input("digite o num de habitantes cidade a:"))
b = int(input("digite o num de habitantes da cidade b: "))
a1 = float(input("percentual de habitantes a: "))
b1 = float(input("percentual de habitantes cidade b: "))
t=0
while (a < b) :
	a = a+(a*(a1/100))
	b = b+(b*(b1/100))
	t=t +1
print(t)