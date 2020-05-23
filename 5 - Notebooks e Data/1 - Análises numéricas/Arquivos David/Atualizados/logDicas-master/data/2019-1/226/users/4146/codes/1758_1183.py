from numpy import *
num = array(eval(input("Numeros: ")))
i = 0
p = 0
n = 0
w = 0

while(i < size(num)):
	if (num[i] > 0):
		p = p + 1
	i = i + 1
new = zeros(p, dtype=int)

while (n < size(num)):
	if (num[n] > 0):
		new[w] = num[n]
		w = w + 1
	n = n + 1
	
print(new)	
	