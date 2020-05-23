from numpy import*
x = array(eval(input("digite a sequencias de jogadas: ")))
y = array(eval(input("digite jogadas correspondente: ")))
	  
#x[0],x[1],x[2]

#y[0],y[1],y[2]
		 
i= 0
soma1 = 0
soma2 = 0

		 
while (i<size(x)):
	if(x[i] == 33  and y[i] == 22 or x[i] == 22 and y[i] == 11 or x[i] == 11 and y[i] == 33):
		soma1 = soma1 + 1
	elif( y[i] == 33 and x[i] == 22 or y[i] == 22 and x[i] == 11 or y[i] == 11 and x[i] == 33):
		soma2 = soma2 + 1
	i = 1 + i

if (soma1>soma2):
	print(size(x))
	print("EUSAPIA")
elif(soma2>soma1):
	print(size(x))
	print("BARSANULFO")
else:
	print(size(x))
	print("EMPATE")

	  
	  
