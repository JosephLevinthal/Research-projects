from numpy import*

string=(input("Digite uma string: "))

a=0
e=0
i=0
o=0
u=0

for x in range(len(string)):
	if(string[x]=="a"):
		a=a+1
	elif(string[x]=="e"):
		e=e+1
	elif(string[x]=="i"):
		i=i+1
	elif(string[x]=="o"):
		o=o+1
	elif(string[x]=="u"):
		u=u+1

print("a: ",a)
print("e: ",e)
print("i: ",i)
print("o: ",o)
print("u: ",u)