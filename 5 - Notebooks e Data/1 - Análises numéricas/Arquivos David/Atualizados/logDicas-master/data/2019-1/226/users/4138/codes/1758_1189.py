from numpy import *
x = input("insira a string:")

a = x.replace(" ","")
print(a.upper())
i = 0
k = 0
t = -1
msg = ""
v = zeros(len(a), dtype=str)
while(i < len(x)):
	if(x[i]!= " "):
		v[k] = x[t]
		msg = msg + v[k]
		k = k + 1
	t = t - 1
	i = i + 1
	
if(msg == (x.replace(" ",""))):
	print(1)
else:
	print(0)

		
