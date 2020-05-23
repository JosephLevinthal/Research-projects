from numpy import *
e = array(eval(input("jogadas de Eusapia: ")))
b = array(eval(input("jogadas de Barsanulfo: ")))
i = 0
soma_e = 0
soma_b = 0
valor_e = 0
valor_b = 0
while(i < size(e)):
	if(e[i] == 33 and b[i] == 22):
		valor_e = 1
		valor_b = 0
	elif(e[i] == 22 and b[i] == 11):
		valor_e = 1
		valor_b = 0
	elif(e[i] == 11 and b[i] == 33):
		valor_e = 1
		valor_b = 0
	elif(e[i] == 11 and b[i] == 11):
		valor_e = 0
		valor_b = 0
	elif(e[i] == 22 and b[i] == 22):
		valor_e = 0
		valor_b = 0
	elif(e[i] == 33 and b[i] == 33):
		valor_e = 0
		valor_b = 0
	elif(e[i] == 22 and b[i] == 33):
		valor_b = 1
		valor_e = 0
	elif(e[i] == 33 and b[i] == 11):
		valor_b = 1
		valor_e = 0
	elif(e[i] == 11 and b[i] == 22):
		valor_b = 1
		valor_e = 0
	soma_b = soma_b + valor_b
	soma_e = soma_e + valor_e
	i = i + 1
print(size(e))
if(soma_b == soma_e):
	print("EMPATE")
if(soma_b>soma_e):
	print("BARSANULFO")
if(soma_e>soma_b):
	print("EUSAPIA")
	