from numpy import*
from math import*

x = array(eval(input("vetor: ")))

m = sum(x)/size(x)
n = 0 

for i in x:
	if n == 0:
		n = n + abs(i - m)
	else:
		n = n * abs(i - m)
n = n ** (1/size(x))
print(round(n, 3))