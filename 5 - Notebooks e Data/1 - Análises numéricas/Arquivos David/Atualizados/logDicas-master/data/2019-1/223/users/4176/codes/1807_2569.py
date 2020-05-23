from numpy import*
x = array(eval(input("Digite: ")))
m = mean(x)
n = size(x)
p = 0
for i in range(size(x)):
	p = p + (x[i] - m)**2
div = p/(n -1)
	
d = (div)**0.5
print(round(d,3))