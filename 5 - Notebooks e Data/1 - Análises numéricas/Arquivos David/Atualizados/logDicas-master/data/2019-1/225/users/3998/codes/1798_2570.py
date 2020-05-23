from numpy import*

x = array(eval(input("vetor: ")))
m = sum(x)/size(x)
j= 1

for i in range(size(x)):
	j= j * abs(x[i]-m)
p = ((j)** (1/size(x)))

print(round(p,3))