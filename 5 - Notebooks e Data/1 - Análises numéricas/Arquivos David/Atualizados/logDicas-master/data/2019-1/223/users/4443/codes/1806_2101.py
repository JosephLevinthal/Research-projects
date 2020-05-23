from numpy import *
n = int(input("Digite um numero inteiro, maior que 2: "))
vec = zeros(n, dtype=int)
vec[0] = 0
vec[1] = 1
i = 2
while(i < n):
	vec[i] = vec[i-2] + vec[i-1]
	i = i+1
print(vec)	