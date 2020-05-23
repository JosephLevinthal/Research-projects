from numpy import *
a = array(eval(input("nota: ")))
b = array(eval(input("alunos: ")))
f = 0
ap = 0
rp = 0
me = 0
ma = 0
i = 0
while( i < size(a)):
	if (a[i] == -1):
		f = f+1
	if (a[i] >= 6):
		ap = ap + 1
	if (a[i] > -1 and a[i] <6):
		rp = rp +1 
	if (a[i] > -1 ):
		me = me + a[i]
	if (a[i] == max(a)):
		ma = b[i]
	i = i + 1
print(f)
print(ap)
print(rp)
print(round((me/(ap+rp)), 2))
print(ma)