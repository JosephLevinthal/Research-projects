from numpy import *
v = input()
r = zeros(5, dtype=int)
for x in range (len(v)):
	if(v[x] == 'a'):
		r[0] = r[0] +1
	elif(v[x] == 'e'):
		r[1] = r[1] +1
	elif(v[x] == 'i'):
		r[2] =r[2] +1
	elif(v[x] == 'o'):
		r[3] = r[3] +1
	elif(v[x] == 'u'):	
		r[4] = r[4] +1
print('a:',r[0])
print('e:', r[1])
print('i:', r[2])
print('o:', r[3])
print('u:', r[4])
		