from numpy import*

x = array(eval(input("v de n reais:")))
n = size(x)
m = mean(x)
p = 1

for i in range(size(x)):
	a = abs(x[i] - m)
	p = p * a
b = (p)**(1/n)
b = round(b,3)
print(b)
	
	