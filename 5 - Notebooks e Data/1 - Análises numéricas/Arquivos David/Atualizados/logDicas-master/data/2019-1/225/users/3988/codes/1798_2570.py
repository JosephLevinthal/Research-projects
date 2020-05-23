from numpy import*
x = array(eval(input("Vetor: ")))

m = sum(x)/size(x)
p1 = 0
for i in range(size(x)):
	if (p1 == 0):
		p1 = abs(x[i] - m)
	elif (p1 > 0):
		p1 = p1 * abs (x[i] - m)
n = size(x)
p = (p1) ** (1/size(x))
print(round(p, 3))