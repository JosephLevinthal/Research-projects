from numpy import*
vetor = array(eval(input("vetores: ")))
i = 0
x = size(vetor)
y = 0

while( i != x):
	y = y + vetor[i] ** (1/3)
	i = i + 1

	h = (y / x) ** 3
print(round(h, 2))