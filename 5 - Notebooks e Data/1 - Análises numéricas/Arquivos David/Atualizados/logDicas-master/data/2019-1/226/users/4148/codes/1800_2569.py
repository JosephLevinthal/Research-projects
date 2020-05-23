from numpy import*

j = array(eval(input('')))

m = sum(j)/size(j) 

a=0

for i in range(size(j)):
	a = a + (j[i] - m) ** 2

d = round((a/(size(j)-1))**(1/2), 3)
	
print(d)