from numpy import*

x=input("")

v=0
c=0

for i in range(len(x)):
	if x[i]=="a" or x[i]=="e" or x[i]=="i" or x[i]=="o" or x[i]=="u":
		v+=1
	if x[i]=="b" or x[i]=="c"or x[i]=="d" or x[i]=="f" or x[i]=="g" or x[i]=="h" or x[i]=="j" or x[i]=="k" or x[i]=="l" or x[i]=="m" or x[i]=="n" or x[i]=="p" or x[i]=="q" or x[i]=="r" or x[i]=="s" or x[i]=="t" or x[i]=="v" or x[i]=="w" or x[i]=="z" or x[i]=="x" or x[i]=='y' :
		c+=1
print(v)
print(c)