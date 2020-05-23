from numpy import *
x = array(eval(input("v: ")))

b = 0
m = sum(x)/size(x)
for i in range(size(x)):
	b = b + (x[i]-m)**2
d = round((b/(size(x)-1))**(1/2), 3)
print(d) 