from numpy import *

vec1 = array(eval(input("Digite ")))
vec2 = array(eval(input("Digite ")) )

i = 0
while (i <= 11):
	if(vec1[i] == max(vec1)):
		print(i+1)
	i += 1