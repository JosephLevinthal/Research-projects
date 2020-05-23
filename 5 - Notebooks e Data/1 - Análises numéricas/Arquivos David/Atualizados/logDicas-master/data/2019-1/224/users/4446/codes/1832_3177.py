from numpy import *
s=input("digite a palavra: ")
a=0
e=0
vi=0
o=0
u=0
for i in s:
	if(i=="a"):
		a=a+1
	if(i=="e"):
		e=e+1
	if(i=="i"):
		vi=vi+1
	if(i=="o"):
		o=o+1
	if(i=="u"):
		u=u+1
print("a:", a)
print("e:", e)
print("i:", vi)
print("o:", o)
print("u:", u)