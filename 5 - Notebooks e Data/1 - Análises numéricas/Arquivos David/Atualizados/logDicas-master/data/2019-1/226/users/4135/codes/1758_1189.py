from numpy import*

v = input("Insira uma string:")

msg = v.replace(" ","")
print(msg.upper())

x = len(v.replace(" ",""))

i = 0
k = 0
a = -1
msg2 = ""

v2 = zeros(x,dtype=str)

while(i < len(v)):
	if(v[a] != " "):
		v2[k] = v[a]
		msg2= msg2 + v2[k]
		k = k + 1
	a = a - 1
	i = i + 1
if(msg2 == (v.replace(" ",""))):
	h = 1
else:
	h = 0
print(h)	

