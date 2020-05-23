from numpy import *

s = input("Digite: ")

n = s[0:3]
j = 3
i = 3
k = 6

while( j < len(s) ):
	n += "." + s[i:k]
	i+=3
	k+=3
	j+=3
	
print(n)

