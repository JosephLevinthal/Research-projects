from numpy import *

v = array(eval(input("Insira as notas: ")))

i = 0
m = 0

while(i < size(v)):
	
	m = m + (v[i]*(i + 1))
	i = i + 1
	
r = 0
c = 0
while(r < size(v)):
	c = c  + (r + 1)
	r = r + 1

media = m/c
print(round(media, 2))