from numpy import*
n = array(eval(input("vetor n:")))
i = 0
m = 0
while (i < size(n)):
	m = (m +( n[i]**(-1)) / size(n))**(-1)
	i = i + 1
print(round(m , 2))