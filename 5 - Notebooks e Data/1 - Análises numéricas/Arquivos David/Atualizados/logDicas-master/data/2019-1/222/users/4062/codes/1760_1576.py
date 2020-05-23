from numpy import*
#entradas 11=pedra, 22=papel e 33=tesoura
a = array(eval(input("sequencia: ")))
b = array(eval(input("sequencia: ")))
i = 0
ca = 0
cb = 0
while(i < size(a) or i <size(b)):
	if((a[i] == 11) and (b[i] == 22)):
		cb = cb + 1
	elif((a[i] == 11) and (b[i] == 33)):
		ca = ca + 1
	elif((a[i] == 22) and (b[i] == 11)):
		ca = ca + 1
	elif((a[i] == 22) and (b[i] == 33)):
		cb = cb + 1
	elif((a[i] == 33) and (b[i] == 22)):
		ca = ca + 1
	elif((a[i] == 33) and (b[i] == 11)):
		cb = cb + 1
	elif(a[i] == b[i]):
		ca = ca + 0
		cb = cb + 0
	i = i + 1
print(size(a))
if(ca > cb):
		print("eusapia".upper())
elif(cb > ca):
		print("barsanulfo".upper())
else:
		print("empate".upper())
		