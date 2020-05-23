from numpy import*
x = array(eval(input("numeros reais:")))
m = sum(x)/size(x)
s = 1
for i in range(size(x)):
	s = s * abs(x[i] - m)
p = (s) ** (1/size(x))
print(round(p,3))