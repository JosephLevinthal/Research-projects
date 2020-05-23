from numpy import *
x = array(eval(input()))
m = sum(x) / size(x)
#m = mean(x)
p = 1
for i in range(size(x)):
	p = ((abs((x[i])-m)))*p
	c = p**(1/size(x))
	#f = sum(p)**()
	
print(round(c, 3))