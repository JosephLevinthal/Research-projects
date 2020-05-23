from numpy import*
n = array(eval(input("Insira um vetor: \n")))

i = 0
m = 0

while(i < size(n)):
	m = m + n[i]**5
	i = i + 1
media = m / size(n)
	s = m *(1/5)
print(round(m , 2))
