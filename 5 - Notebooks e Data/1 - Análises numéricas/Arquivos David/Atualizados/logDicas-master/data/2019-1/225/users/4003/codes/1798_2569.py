from numpy import*

x = array(eval(input("x:")))
m = sum(x)/size(x)
j = 0
for i in range(size(x)):
	j = j + (x[i] - m)**2
	
d = sqrt(j/(size(x)-1))

print(round(d,3))