from numpy import *

x = array(eval(input()))
y = array(eval(input()))

e = 0
ve = 0
vb = 0
h = 0



while size(x) > h:
	if x[h] == y[h]:
		e += 1
	elif x[h] == 11 and y[h] != 22:
		ve += 1
	elif x[h] == 22 and y[h] != 33:
		ve += 1
	elif x[h] == 33 and y[h] != 11:
		ve += 1
	else:
		vb += 1
	h += 1 

if ve > vb:
	f = ("EUSAPIA")
if vb > ve:
	f = ("BARSANULFO")
if ve == vb:
	f = ("EMPATE")
	
print(h)
print(f)