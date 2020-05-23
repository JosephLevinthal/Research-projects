from numpy import*

z=input()
va=0
ve=0
vi=0
vo=0
vu=0
for i in range(len(z)):
	if(z[i]=='a'):
		va+=1
	elif(z[i]=="e"):
		ve+=1
	elif(z[i]=="i"):
		vi+=1
	elif(z[i]=="o"):
		vo+=1
	elif(z[i]=="u"):
		vu+=1
print("a:",va)
print("e:",ve)
print("i:",vi)
print("o:",vo)
print("u:",vu)