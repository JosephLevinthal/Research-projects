from numpy import *
n = int(input("entre com o numero de asteristicos: "))
s = []
v = []
x = n*2
c=1
z= n-1
while(c<=x):
	s.append('*')
	c = c + 1
v = str(s).strip('[]')
v = (v,end='')
print (v)