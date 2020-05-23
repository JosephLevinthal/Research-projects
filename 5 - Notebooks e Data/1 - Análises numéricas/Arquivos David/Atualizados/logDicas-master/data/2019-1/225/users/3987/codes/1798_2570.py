from numpy import*

n = array(eval(input("n:")))
m = sum(n)/size(n)
j=1
for i in range(size(n)):
	j = j * abs(n[i] - m)
	
p = ((j)**(1/size(n)))
print(round(p,3))