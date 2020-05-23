from numpy import*
x = array(eval(input("x: ")))

n = 1
d1 = 0
m = sum(x)/size(x)

for i in range(size(x)):
	d1 = d1 + (x[i] - m)**2
d2 = sqrt(d1/(size(x) - 1))
print(round(d2, 3))


