from numpy import *
mf = array(eval(input("digite o vetor : ")))
frequencia = array(eval(input("digite as horas: ")))
horas = array(eval(input("digite as horas : ")))
a = 0
r = 0
rf = 0
for x,y in zip(mf,frequencia):
	
	if(x>=5 and y >= (75/100)*horas):
		a = a + 1
	if(x < 5):
		r = r + 1
	if(y < (75/100) * horas):
		rf = rf + 1

z = zeros(3,dtype= int)		
z[0] = a
z[1] = r
z[2] = rf
print(z)
		
		
		
	