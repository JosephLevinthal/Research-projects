from numpy import*

x = array(eval(input("v de n reais:")))
n = size(x)
m = mean(x)
p = 0 

for i in range(size(x)):
	p = p + (x[i] - m)**2
	divisor = p/(n - 1)
a = (divisor)**0.5
a = round(a,3)
print(a)
	