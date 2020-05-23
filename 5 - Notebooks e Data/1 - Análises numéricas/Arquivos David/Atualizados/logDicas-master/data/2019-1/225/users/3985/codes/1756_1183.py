from numpy import *

vec = array(eval(input("vetor de numeros")))
i = 0
pos = 0
while (i < size(vec)):
	if (vec[i] >= 0):
		pos += 1
	i += 1

vec2 = zeros(pos, dtype = int)
i = 0
j = 0
while (i < size(vec)):
	if (vec[i] >= 0):
		vec2[j] = vec[i]
		j += 1
	i += 1
print(vec2)