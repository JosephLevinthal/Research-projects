from numpy import *

n = array(eval(input('N: ')))
q = array(eval(input('Q: ')))

total = 0 

for i in range(size(n)):
	if n[i]=='ARROZ':
		a = 1.25*q[i]
	if n[i]=='FEIJAO':
		a = 2.60*q[i]
	if n[i]=='BIS':
		a==1.80*q[i]
	if n[i]=='MIOJO':
		a = 0.85*q[i]
	if n[i]=='FANTA':
		a = 3.20*q[i]
print(round(sum(a), 2))