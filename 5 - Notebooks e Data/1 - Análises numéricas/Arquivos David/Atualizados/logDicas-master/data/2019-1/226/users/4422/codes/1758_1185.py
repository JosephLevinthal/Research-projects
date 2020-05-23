from numpy import*
g = array(eval(input("Vetor: ")))

i = 0
n = 0

while(i<size(g)):
	if(g[i]>99):
		n = n + 1
		i = i + 1
		print(i-1)
	else:
		i = i + 1
print(n)