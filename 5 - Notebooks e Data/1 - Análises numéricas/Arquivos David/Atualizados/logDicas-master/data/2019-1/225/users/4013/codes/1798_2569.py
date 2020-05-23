from numpy import*
x = array(eval(input("vetor de num reais:")))
m = sum(x)/size(x)
s = 0
for i in range(size(x)):
	s = s + (x[i] - m)**2
d = sqrt(s / (size(x) - 1)) 
print(round(d, 3))