from numpy import*

x = array(eval(input("digite as notas: ")))
a = 0
for i in range(size(x)):
	if(x[i]<5):
		a = a + 1
rep = zeros(a, dtype= int)
y = 0
j = 0
print(a)
for k in range(size(x)):
	if(x[j]<5):
		rep[y]= j
		y = y + 1
	j = j + 1
print(rep)	