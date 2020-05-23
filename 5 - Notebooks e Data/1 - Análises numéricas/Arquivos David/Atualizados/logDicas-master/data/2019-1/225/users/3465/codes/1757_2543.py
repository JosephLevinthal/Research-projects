from numpy import *
p = array(eval(input("")))
string = ''
for i in range(len(p)-1):
	string+=str(p[i])+"x^"+str((len(p)-1)-i)+" + "
string = string.replace("^1",'')
string+=str(p[-1])
print(string)