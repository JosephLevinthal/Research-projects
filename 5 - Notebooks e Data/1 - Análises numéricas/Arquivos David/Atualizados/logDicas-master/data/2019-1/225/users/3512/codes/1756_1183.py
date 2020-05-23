from numpy import *

anderson= array(eval(input("elemetary: ")))
cont = 0
var = []

while ( cont < size(anderson)):
	if(anderson[cont] >= 0):
		var.append(anderson[cont])
	cont = cont + 1 
	
print(str(var).replace(',', ''))