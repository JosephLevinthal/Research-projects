from numpy import*

N = array(eval(input("Notas: ")))
c = arange(size(N)+1)
i = 0
x = 1
n = 0
while(i < size(N)):
	n = N[i] * x + n
	x = x + 1
	i = i + 1
print(round(n/sum(c), 2))
