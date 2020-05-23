from numpy import*
x = array(eval(input("vetor: ")))
m = sum(x)/size(x)
s = 1
for i in range(size(x)):
	s = abs(s * (x[i]-m))
p = s**(1/size(x))
print(round(p, 3))