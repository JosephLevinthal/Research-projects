from numpy import*
v= array(eval(input("Vetor: ")))
x = zeros(size(v),dtype=int)
i=0

for i in range(size(v)):
	j = size(v) - i - 1
	x[j] = v[i]
	aux = v[i] + 1
	i = i + 1
print(x)