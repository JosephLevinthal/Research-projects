from numpy import*
x = array(eval(input("vetor decrescente: ")))

y = zeros(size(x), dtype=int)
z = -1

for i in x:
	y[z] = i
	z = z - 1
print(y)