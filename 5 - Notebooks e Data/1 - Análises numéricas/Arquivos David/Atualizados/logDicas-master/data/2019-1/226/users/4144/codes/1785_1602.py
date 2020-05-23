from numpy import *
a = array(eval(input("digite as chegadas: ")))
i = 0

while(i<size(a)):
	if(a[i]==max(a)):
		print(i)
	i = i +1
