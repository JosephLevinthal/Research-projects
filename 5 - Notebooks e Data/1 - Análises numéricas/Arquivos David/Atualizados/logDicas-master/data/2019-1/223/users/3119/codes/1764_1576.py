from numpy import*

eus = array(eval(input("Digite as jogadas de eusapia: ")))
bar = array(eval(input("Digite as jogadas de Barsanulfo: ")))

i = 0
e = 0
b = 0

while(i < size(eus) and i < size(bar)):
	if((eus[i] == 11 and bar[i] == 33) or (eus[i] == 22 and bar[i] == 11) or (eus[i] == 33 and bar[i] == 22)):
		e = e + 1
	if((bar[i] == 11 and eus[i] == 33) or (bar[i] == 22 and eus[i] == 11) or (bar[i] == 33 and eus[i] == 22)):
		b = b + 1
	else:
		e = e + 0
		
	i = i + 1	

print(i)
e
b

if(e > b):
	print("EUSAPIA")
elif(e == b):
	print("EMPATE")
else:
	print("BARSANULFO")

	
	

