from numpy import*

es = input("digite o estado: ").upper().split(',')

a = zeros(5, dtype=int)
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
for i in range(size(es)):
		if	(es[i] == 'AC'):
			a1 = a1 + 1
		elif	(es[i] == 'AM'):
				a2 = a2 + 1
		elif	(es[i] == 'PA'):
				a3 = a3 + 1
		elif	(es[i] == 'RO'):
				a4 = a4 + 1
		elif	(es[i] == 'RR'):
				a5 = a5 + 1
				
		a[0] = a1
		a[1] = a2
		a[2] = a3
		a[3] = a4
		a[4] = a5
print(max(a))
print(a)
			