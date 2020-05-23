from numpy import*
x= int(input("qual seu numero de asteriscos?"))

for i in range(x):
	print((x-i)*'*' + 2*i*'o'+(x-i)*'*')
	
	
	