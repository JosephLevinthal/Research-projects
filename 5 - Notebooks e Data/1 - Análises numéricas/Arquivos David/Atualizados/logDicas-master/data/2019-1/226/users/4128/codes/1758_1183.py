from numpy import*

x = array(eval(input("vetores:")))
i = 0 #contadora
n = 0 #negativos
while(i < size(x)):
	if(x[i] < 0):
		n = n + 1
	i = i + 1

tf = size(x) - n
vf = zeros(tf,dtype = int)
j = 0
i = 0

while(i <size(x)):
	if (x[i])>=0 :
		vf[j] = x[i]
		j =j + 1
	i = i + 1
print(vf)	
	