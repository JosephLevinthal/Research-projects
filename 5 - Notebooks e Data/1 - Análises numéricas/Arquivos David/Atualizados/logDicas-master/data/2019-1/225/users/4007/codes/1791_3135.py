from numpy import*
v = array(eval(input("vetor: ")))
i = 0
s = 0
a = 0
while (i < size(v)):
	s = s + v[i] ** 0.5 
	i = i + 1
a = (s / size(v))**2
print(round(a, 2))
	
	