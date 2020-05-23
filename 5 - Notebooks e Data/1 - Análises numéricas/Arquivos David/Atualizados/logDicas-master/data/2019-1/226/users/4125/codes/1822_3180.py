from numpy import*

x = array(eval(input("digite os pacientes diagnosticados com dengue: ")))
a = zeros(4, dtype= int)
for i in range(size(x)):
	if (x[i]==1):
		a[0]= a[0] + 1
	elif(x[i]==2):
		a[1]= a[1] + 1
	elif(x[i]==3):
		a[2]= a[2] + 1
	elif(x[i]==4):
		a[3]= a[3] + 1
print(a)