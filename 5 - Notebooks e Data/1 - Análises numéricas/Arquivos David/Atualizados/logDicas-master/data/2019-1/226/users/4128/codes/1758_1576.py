from numpy import*

e = array(eval(input("joquempo:")))
b = array(eval(input("pedra, papel, tesoura:")))

y = 0 #eusapia
x = 0 #barasanulfo
i = 0
while(i < size(e)):
	if(e[i] == 11 and b[i] == 33) or (e[i] == 22 and b[i] == 11) or (e[i] == 33 and b[i] == 22):
		y = y + 1
	elif(b[i] == 11 and e[i] == 33) or (b[i] == 22 and e[i] == 11) or (b[i] == 33 and e[i] == 22):
		x = x + 1
		
	i = i + 1
if(x > y):
	print(i)
	print("BARSANULFO")
elif(y > x):
	print(i)
	print("EUSAPIA")
else:
	print(i)
	print("EMPATE")
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		