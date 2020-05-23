from numpy import *
ve = array(eval(input("Digite os coeficientes da equacao: ")))
n = len(ve)
i = 0
vs = ""
exp = 0
while(i<n):
	co = str(ve[i])
	exp = (n-1) - i
	if(exp > 1):
		exp = str(exp)
		vs = vs + co+"x^"+ exp + " + "
	elif(exp > 0):	
		exp = str(exp)
		vs = vs + co+"x + "
	elif(exp == 0)	:
		vs = vs + co
	i = i+1
print(vs)		
	
	