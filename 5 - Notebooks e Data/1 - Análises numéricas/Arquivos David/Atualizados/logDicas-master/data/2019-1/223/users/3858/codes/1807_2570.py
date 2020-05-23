from numpy import *
from math import *
v = array(eval(input()))

p = 0
soma = 0
total = 0
for x in range (size(v)):
	soma = soma + v[x]
	print(v[x])
media = soma/size(v)

for x in range(size(v)-1):
	p = p + abs(v[x]-media) * abs(v[x+1] - media)
total = p**(1/(size(v)))
print(round(total,3))